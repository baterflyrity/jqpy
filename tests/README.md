<!-- TOC -->
* [Running tests](#running-tests)
  * [Updating upstream tests](#updating-upstream-tests)
* [Known issues](#known-issues)
* [Writing tests](#writing-tests)
  * [Creating test script](#creating-test-script)
  * [Creating jq test file](#creating-jq-test-file)
<!-- TOC -->

# Running tests

Tests are evaluated using [pytest](https://docs.pytest.org/) runner. Also, custom parser is used to evaluate [upstream](https://github.com/jqlang/jq/tree/master/tests/) tests.

```shell
cd tests
pip install -r requirements.txt
pytest
```

## Updating upstream tests

Optionally actual upstream tests can be fetched with [fetch_upstream.bat](fetch_upstream.bat) for Windows or [fetch_upstream.sh](fetch_upstream.sh) for Linux.

```shell
cd tests
pip install -r requirements.txt
bash fetch_upstream.sh
pytest
```

# Known issues

JQpy considers common [upstream](https://github.com/jqlang/jq/tree/master/tests/) test cases along with binding-specific pythonic.

For upstream cases there are known fail cases. These cases are responsibility of upstream developers but JQpy - please, comment linked upstream issues.

**Module or variable is missing**

<small>*test_upstream → test_jq → case 334, 335, 336, 337, 338, 339, 340, 341, 348, 349, 350, 351, 353*, *test_upstream → test_man → case 156, 157*</small>

Several upstream cases require special environment which is not reproduced by JQpy. Thus, such cases always fail.

**NaN, None, null, numbers confusion**

<small>*test_upstream → test_jq → case 423*, *test_upstream → test_man → case 4*</small>

In rare cases JQpy upstream test file parser can ignore detailed missing number values like `NaN` and convert them to pythonic `None`. Basically this is not an issue because JQpy expected to work **only with pythonic JSON-compatible types** (`Union[None, bool, int, float, str, Dict, List]`). Other types (including `NaN`) are neither JSON-compatible nor pythonic hence simply converted to `None`.

Same rules are applied to any non-pythonic numbers representation like, e.g. 1.0000 → 1.0, 100e-2 → 1.0.

[**Unreadable characters**](https://github.com/jqlang/jq/issues/2961/)

<small>*test_upstream → test_jq → case 329*, *test_upstream → test_optional → case 2*</small>

In some environments jq produces unreadable corrupted characters like `�������, ���� 30, 2015` instead of `Tuesday, June 30, 2015`.

[**Wrong math**](https://github.com/jqlang/jq/issues/2962/)

<small>*test_upstream → test_jq → case 391, 392, 393*</small>

Somehow jq broke big numbers arithmetic due to mixing bigint, dec and double types. This should be fixed in future release.

# Writing tests

There are two supported formats of tests:

1. define python test script;
2. write jq test file (*\*.test*).

It is strongly recommended to use the first way and write separate test scripts.

## Creating test script

1. Create script with *test_* prefix, e.g. *tests/test_feature42.py*.
2. Write some [pytest](https://docs.pytest.org/en/7.4.x/how-to/assert.html) cases:

```python
from runner import jq


def test_feature_42():
	assert jq('42') == [42]
```

3. Ensure tests pass:

```shell
$ cd tests
$ pytest test_feature42.py 
==================== test session starts ==================
platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
rootdir: ...\jqpy\tests
plugins: anyio-3.7.1, Faker-19.12.0
collected 1 items

test_binding.py .....                                [100%]

==================== 1 passed in 0.23s ==================== 
```

## Creating jq test file

Jq originally provides specially formatted text files with *\*.test* extension to defined test cases. **These files are [intended to be utilized internally](https://github.com/jqlang/jq/issues/2939#issuecomment-1789771102) and should not be used by anyone.**

> What of this? What's the problem with this? Yes, it's at the start of a line, so what? This is NOT a JSON file. This is NOT a file with any format that any other tool should support. This is a file used internally by jq. Bindings for Python or whatever language should NOT use this file. You can adapt tests from this file to test your bindings, sure, but with some care.

Hence, one desiring to write test file should ask for help in upstream issue tracker. However, jqpy provides special parser for such files using [PEG-like grammars](https://textx.github.io/textX/stable/grammar):

* One [grammar](testfile_parser/grammar.py) for obtaining cases from test file:

```
TestFile: cases*=TestCase[/\n(\s*\n)*/];
TestCase: /\s*/- (AnyErrorCase | FixedErrorCase | OutputCase);

AnyErrorCase: '%%FAIL IGNORE MSG' '\n' program=Line '\n' Line*['\n'];
FixedErrorCase: '%%FAIL' '\n' program=Line '\n' error=Line ('\n' Line*['\n'])?;
OutputCase: program=Line '\n' input=Line '\n' outputs*=Line['\n'];

Line: /[^\n]*/;
Comment: /^#.*$/; // this just not works :(
```

* Another [grammar](json_parser/grammar.py) for converting data to JSON-compatible pythonic types:

```
File: Array | Object | Value;

Array: "[" values*=Value[','] "]";

Value: Infinity | Null | Nan | STRING | NUMBER | BOOL | Object | Array;

Null: "null";

Object: "{" members*=Member[','] "}";

Member: key=STRING ':' value=Value;

Infinity[noskipws]: negotiation?="-" "Infinity";

Nan[noskipws]: "-"? "NaN";
```

After creating test file, e.g. *tests/feature35.test*, it should be evaluated with pytest case script, e.g. *tests/test_feature35.py*:

```python
import pytest
from runner import collect_tests_from_file, run_case


@pytest.mark.parametrize(['case'], collect_tests_from_file('feature35.test'))
def test_feature_35(case):
	run_case(case)
```

Now testfile can be evaluated with pytest. Example for [manonig.test](manonig.test):

```shell
$ cd tests
$ pytest test_upstream.py::test_manonig
================== test session starts ====================
platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
rootdir: ...\jqpy\tests
plugins: anyio-3.7.1, Faker-19.12.0
collected 17 items

test_upstream.py .................                   [100%]
================== 17 passed in 7.95s =====================
```
