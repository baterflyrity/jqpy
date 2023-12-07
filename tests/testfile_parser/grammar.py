GRAMMAR = r"""


TestFile: cases*=TestCase[/\n(\s*\n)*/];
TestCase: /\s*/- (AnyErrorCase | FixedErrorCase | OutputCase);

AnyErrorCase: '%%FAIL IGNORE MSG' '\n' program=Line '\n' Line*['\n'];
FixedErrorCase: '%%FAIL' '\n' program=Line '\n' error=Line ('\n' Line*['\n'])?;
OutputCase: program=Line '\n' input=Line '\n' outputs*=Line['\n'];

Line: /[^\n]*/;
Comment: /^#.*$/; // this just not works :(


"""
