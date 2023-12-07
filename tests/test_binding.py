from runner import jq


def test_multiline():
	assert jq(r'.[] | test("a b c # spaces are ignored"; "ix")', ["xabcd", "ABC"]) == [True, True]


def test_empty_filter():
	assert jq(data=123) == [123]


def test_empty_input():
	assert jq('1') == [1]


def test_empty_input_filter():
	assert jq() == []


def test_feature_42():
	assert jq('42') == [42]
