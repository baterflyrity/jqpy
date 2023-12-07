import ast
import sys
from functools import lru_cache

from textx import metamodel_from_str

from jqpy import JSON
from json_parser.grammar import GRAMMAR

processors = {}


def _rule(rule: str):
	def decorator(f):
		processors[rule] = f
		return f

	return decorator


@_rule('Array')
def _handle_array(x):
	return list(x.values)


@_rule('Object')
def _handle_object(x):
	return {member.key: member.value for member in x.members}


@_rule('Null')
def _handle_null(x):
	return None


@_rule('Infinity')
def _handle_infinity(x):
	if x.negotiation:
		return -sys.float_info.max
	return sys.float_info.max


@_rule('Nan')
def _handle_nan(x):
	return None


@_rule('STRING')
def _handle_string(x: str):
	assert x.startswith(('"', "'")) and x.endswith(('"', "'")), f'Unterminated string: {x}'
	return ast.parse(f'"""{x[1:-1]}"""').body[0].value.value


@lru_cache()
def _get_meta_model():
	mm = metamodel_from_str(GRAMMAR, skipws=True, ignore_case=True, debug=False)
	mm.register_obj_processors(processors)
	return mm


def _remove_prefix(text, prefix):
	return text[text.startswith(prefix) and len(prefix):]


def parse_json(string: str) -> JSON:
	string = _remove_prefix(string, '\ufeff')  # BOM
	mm = _get_meta_model()
	try:
		model = mm.model_from_str(string)
	except Exception as e:
		raise ValueError(f'Can not parse JSON: {e}') from e
	if model.__class__.__name__ in processors:
		return processors[model.__class__.__name__](model)
	return model
