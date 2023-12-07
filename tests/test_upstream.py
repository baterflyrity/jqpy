import pytest

from runner import collect_tests_from_file, run_case


@pytest.mark.parametrize(['case'], collect_tests_from_file('base64.test'))
def test_base64(case):
	run_case(case)


@pytest.mark.parametrize(['case'], collect_tests_from_file('jq.test'))
def test_jq(case):
	run_case(case)


@pytest.mark.parametrize(['case'], collect_tests_from_file('man.test'))
def test_man(case):
	run_case(case)


@pytest.mark.parametrize(['case'], collect_tests_from_file('manonig.test'))
def test_manonig(case):
	run_case(case)


@pytest.mark.parametrize(['case'], collect_tests_from_file('onig.test'))
def test_onig(case):
	run_case(case)


@pytest.mark.parametrize(['case'], collect_tests_from_file('optional.test'))
def test_optional(case):
	run_case(case)
