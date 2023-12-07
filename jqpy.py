"""JQpy is Python binding for JQ (JSON processing language) that simply works on any platform (even Windows) and does not require compilation."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from json import JSONDecodeError
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict, List, Optional, Union

__version__ = '1.0.0'

JSON = Union[None, bool, int, float, str, Dict, List]
"""
JSON serializable type.
"""


class _TEmptyInput:
	pass


EmptyInput = _TEmptyInput()
"""
Constant that represents no data input.

None can not be used because it is valid JSON value.
"""


class JQError(Exception):
	"""
	Base jqpy exception.
	"""
	pass


class JQMissingError(JQError):
	"""
	Jq binary executable (typically jq.exe in Windows and /usr/bin/jq in Unix) ws not found.

	Jq binary can be installed via system package manager or from https://jqlang.github.io/jq/download official website.
	"""
	pass


class JQProcessingError(JQError):
	"""
	Processing was not finished successfully.
	"""
	pass


class JQRuntimeError(JQProcessingError):
	"""
	Processing was failed.
	"""
	pass


class JQResultError(JQRuntimeError):
	"""
	Result of processing was corrupted.
	"""
	pass


class JQUsageError(JQRuntimeError):
	"""
	Processing was aborted of finished with errors.
	"""
	pass


class JQTimeoutError(JQProcessingError):
	"""
	Processing took too much time.

	By default, processing longer then 5 minutes will rise this error.
	"""
	pass


@dataclass
class RawOutput:
	"""
	Raw jq binary evaluation results.
	"""

	stdout: str
	"""
	Standard output text of jq evaluation.
	"""
	stderr: str
	"""
	Standard error text of jq evaluation.
	"""
	code: int
	"""
	Return code of jq evaluation.
	"""
	filter: str
	"""
	Processed jq filtration program.
	"""

	@property
	def text(self) -> str:
		"""
		Combined stdout then stderr texts.

		Result is joined with new line and stripped.
		"""
		return f'{self.stdout}\n{self.stderr}'.strip()

	@property
	def json_output(self) -> List[JSON]:
		"""
		List of JSON parsed results from jq evaluation one per each line.

		:raise JQResultError: jq evaluation resulted in bad output.
		"""
		return _parse_output(self.stdout, self.filter)


def _parse_output(text: str, jq_filter: str) -> List[JSON]:
	text = text.replace('\r\n', '\n').strip()
	if not text:
		return []
	try:
		return [json.loads(data) for data in text.split('\n') if data.strip()]
	except JSONDecodeError as e:
		raise JQResultError(f'Received bad output from jq. Can not detect result from string: {text}\n\nFiltration command: {jq_filter}') from e


def jq(filter: str = '', data: Union[JSON, _TEmptyInput] = EmptyInput, *, timeout: Optional[float] = 300, raw_output: bool = False) -> Union[List[JSON], RawOutput]:
	"""
	Evaluate jq with provided input JSON data and filtration program.

	:param filter: jq filtration program. By default, is empty.
	:param data: JSON compatible input data to be passed to jq. By default, is empty.
	:param timeout: jq evaluation maximum time. By default, processing longer then 5 minutes will rise JQTimeoutError error.
	:param raw_output: whether to return raw results of jq evaluation. In the most cases integrated JSON data results parser should be used instead.
	:return: List of JSON parsed results from jq evaluation one per each line.
	:raise ValueError: invalid input data was provided.
	:raise JQMissingError: jq binary dependency not found.
	:raise JQUsageError: jq evaluation failed.
	:raise JQTimeoutError: jq evaluation took too much time.
	:raise JQResultError: jq evaluation resulted in bad output.
	"""
	if not filter.strip():
		if data is EmptyInput:
			return []
		return [data]
	args = ['--monochrome-output', '--compact-output']
	if data is EmptyInput:
		args.append('--null-input')
		data_str = ''
	else:
		try:
			data_str = json.dumps(data, ensure_ascii=False, indent='')
		except Exception as e:
			raise ValueError(f'Bad input data passed to jq. Input must be any JSON compatible object (see https://docs.python.org/3/library/json.html). Given input: {data}') from e
	with NamedTemporaryFile('w+', encoding='utf8', delete=False) as f:
		try:
			f.write(filter)
			f.close()
			args.extend(['--from-file', str(Path(f.name).resolve())])
			try:
				p = subprocess.Popen(args, executable=shutil.which('jq'), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, encoding='utf8')
				p.stdin.write(data_str)
				p.stdin.close()
			except FileNotFoundError as e:
				installation = 'choco install jq' if os.name == 'nt' else 'apt-get install jq'
				raise JQMissingError(f'Can not find jq binary executable (typically jq.exe in Windows and /usr/bin/jq in Unix). Install jq binary via your system package manager or from https://jqlang.github.io/jq/download then restart the program. If you have already installed jq ensure you have jq in PATH environment variable.\nYou can try to install jq binary executable via running "{installation}" command.') from e
			except Exception as e:
				raise JQUsageError(f'Unexpected usage of jq. Filtration was unexpectedly aborted: {e}.\n\nFiltration command: {filter}') from e
			try:
				p.wait(timeout=timeout)
			except subprocess.TimeoutExpired as e:
				p.kill()
				raise JQTimeoutError(f'Filtration timed out and was killed.\n\nFiltration command: {filter}') from e
		finally:
			Path(f.name).unlink(missing_ok=True)
	if raw_output:
		return RawOutput(stdout=p.stdout.read(), stderr=p.stderr.read(), code=p.returncode, filter=filter)
	err = p.stderr.read()
	if p.returncode != 0 or err:
		raise JQUsageError(f'Unexpected usage of jq. Filtration process finished with error code {p.returncode} with error message: {err}\n\nFiltration command: {filter}')
	return _parse_output(p.stdout.read(), filter)
