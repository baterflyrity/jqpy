import sys
from pathlib import Path
from typing import List, Optional, Tuple, Union

sys.path.insert(0, '..')  # add jqpy.py to path
from jqpy import JQError, jq
from testfile_parser.parser import AnyErrorCase, FixedErrorCase, TestCase, parse_testfile


class JQTestError(JQError):
	pass


class JQTestNotFailError(JQError):
	pass


class JQTestBadFailError(JQError):
	pass


class JQTestBadOutputError(JQError):
	pass


class JQTestModuleImportError(JQError):
	pass


def run_case(case: TestCase, *, timeout: Optional[float] = 30):
	"""
	Execute test case and raise one of JQTestError on validation missassertion.

	:param case: case to check.
	:param timeout: maximum jq evaluation time.
	:raise JQTestError: case validation failed.
	:raise JQError: jq evaluation failed.
	"""
	try:
		result = jq(case.program, case.optional_input, timeout=timeout, raw_output=True)
	except Exception as e:
		raise JQTestError(f'Unexpected error occurred while processing case: {e}.\n{case.source}') from e
	if 'module not found' in result.text:
		raise JQTestModuleImportError(f'Module is missing in case: {result.text}\n{case.source}')
	if isinstance(case, AnyErrorCase):
		if 'error' not in result.text:
			raise JQTestNotFailError(f'Asserted error did not occured while processing case.\n{case.source}')
	elif isinstance(case, FixedErrorCase):
		if case.error not in result.text:
			raise JQTestBadFailError(f'Wrong asserted error while processing case. Expected {case.error}.\n{case.source}')
	elif result.json_output != case.outputs:
		raise JQTestBadOutputError(f'Wrong result of processing case: {result.text or "<EOF>"}.\n{case.source}')


def collect_tests_from_file(testfile: Union[Path, str]) -> List[Tuple[TestCase]]:
	"""
	Helper function to test cases from test file.

	:param testfile: path to test file.
	:return: pytest.mark.parametrize formatted cases.
	"""
	return [(case,) for case in parse_testfile(testfile)]
