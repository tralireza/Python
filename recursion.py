from typing import List


class Solution1106:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        1106h Parsing a Boolean Expression
        """

        def parse(icur: List[int]) -> bool:
            print(" ->", expression[icur[0]], icur[0])

            match expression[icur[0]]:
                case "f":
                    icur[0] += 1
                    return False
                case "t":
                    icur[0] += 1
                    return True
                case "!":
                    icur[0] += 2
                    v = not parse(icur)
                    icur[0] += 1
                    return v
                case _:
                    op = expression[icur[0]]
                    vals = []

                    icur[0] += 2
                    while expression[icur[0]] != ")":
                        match expression[icur[0]]:
                            case ",":
                                icur[0] += 1
                            case _:
                                vals.append(parse(icur))
                    icur[0] += 1

                    if op == "&":
                        return all(vals)
                    return any(vals)

        return parse([0])
