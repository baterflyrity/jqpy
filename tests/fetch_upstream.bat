echo off
echo Downloading recent tests from official upstream jq repository at https://github.com/jqlang/jq/tree/master/tests
curl -kLs https://raw.githubusercontent.com/jqlang/jq/master/tests/optional.test -o optional.test
curl -kLs https://raw.githubusercontent.com/jqlang/jq/master/tests/onig.test -o onig.test
curl -kLs https://raw.githubusercontent.com/jqlang/jq/master/tests/manonig.test -o manonig.test
curl -kLs https://raw.githubusercontent.com/jqlang/jq/master/tests/man.test -o man.test
curl -kLs https://raw.githubusercontent.com/jqlang/jq/master/tests/jq.test -o jq.test
curl -kLs https://raw.githubusercontent.com/jqlang/jq/master/tests/base64.test -o base64.test
