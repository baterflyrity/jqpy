GRAMMAR = r"""

File: Array | Object | Value;

Array: "[" values*=Value[','] "]";

Value: Infinity | Null | Nan | STRING | NUMBER | BOOL | Object | Array;

Null: "null";

Object: "{" members*=Member[','] "}";

Member: key=STRING ':' value=Value;

Infinity[noskipws]: negotiation?="-" "Infinity";

Nan[noskipws]: "-"? "NaN";


"""
