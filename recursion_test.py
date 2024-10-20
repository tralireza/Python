import recursion as m


def test_Solution1106():
    # 1106h Parsing a Boolean Expression
    assert m.Solution1106().parseBoolExpr("&(|(f)))") is False
    assert m.Solution1106().parseBoolExpr("|(f,f,f,t)") is True
    assert m.Solution1106().parseBoolExpr("!(&(f,t))") is True
