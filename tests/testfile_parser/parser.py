import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Union

from textx import metamodel_from_str, textx_isinstance

from jqpy import JSON
from json_parser.parser import parse_json
from testfile_parser.grammar import GRAMMAR


@dataclass
class TestCaseBase:
	"""
	Base class for test case.
	"""
	source: str
	"""
	Source lines of case in test file.
	"""
	program: str
	"""
	JQ filter program.
	"""

	@property
	def optional_input(self) -> Optional[JSON]:
		"""
		Input JSON data if any.
		"""
		return getattr(self, 'input', None)


@dataclass
class AnyErrorCase(TestCaseBase):
	"""
	Assert case fails with any error.
	"""
	pass


@dataclass
class FixedErrorCase(TestCaseBase):
	"""
	Assert case fails with specific error.
	"""
	error: str
	"""
	JQ evaluation error message.
	
	Can be incomplete.
	"""


@dataclass
class OutputCase(TestCaseBase):
	"""
	Assert case succeeds with specific JSON output.
	"""
	input: JSON
	"""
	Input JSON data passed to JQ.
	"""
	outputs: List[JSON] = field(default_factory=list)
	"""
	List of multiple JSON outputs provided by JQ.
	
	Appears to contain single output item in most cases.
	"""


TestCase = Union[AnyErrorCase, FixedErrorCase, OutputCase]
"""
Type alias for test case except base class.
"""


def _get_model_source(model, sources: str) -> str:
	return sources[model._tx_position:model._tx_position_end]


def _validate_case(case) -> None:
	assert all([getattr(case, name, False) is not None for name in ['program', 'input', 'outputs', 'error']]), f'Corrupted test case from:\n{case.source}'


def _validate_data(cases: List[TestCaseBase], sources: str) -> None:
	parsed_sources = _normalize_sources('\n'.join([case.source for case in cases]))
	assert parsed_sources == sources, 'Corrupted tests file'


def _normalize_sources(sources: str) -> str:
	sources = sources.replace('\r\n', '\n')
	sources = re.sub(r'^#.*$', '', sources, flags=re.MULTILINE)
	sources = re.sub(r'\n\s*?\n(\s*?\n)+', '\n\n', sources, flags=re.MULTILINE)
	return sources.strip()


def parse_testfile(testfile: Union[Path, str]) -> List[TestCase]:
	"""
	Parse test file.

	:param testfile: path to test file.
	:return: list of parsed test cases.
	"""
	testfile = Path(testfile)
	sources = _normalize_sources(testfile.read_text('utf8'))
	testfile_mm = metamodel_from_str(GRAMMAR, skipws=False, ignore_case=True, debug=False)
	any_error_case = testfile_mm['AnyErrorCase']
	fixed_error_case = testfile_mm['FixedErrorCase']
	testfile_model = testfile_mm.model_from_str(sources, file_name=str(testfile))
	cases = []
	for case in testfile_model.cases:
		src = _get_model_source(case, sources)
		common_args = dict(source=src, program=case.program)
		if textx_isinstance(case, any_error_case):
			data = AnyErrorCase(**common_args)
		elif textx_isinstance(case, fixed_error_case):
			data = FixedErrorCase(error=case.error, **common_args)
		else:
			try:
				data = OutputCase(input=parse_json(case.input), outputs=[parse_json(x) for x in case.outputs], **common_args)
			except ValueError as e:
				raise ValueError(f'Invalid JSON input or output: {e}\n{src}')
		_validate_case(case)
		cases.append(data)
	_validate_data(cases, sources)
	return cases
