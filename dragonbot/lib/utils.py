import re


def regexbuild(li: list, capture = False) -> str:
    """
    regexbuild(["a", "b", "c"])
    >>> "a|b|c"
    regexbuild(["a", "b", "c"], capture = True)
    >>> "(a|b|c)"
    regexbuild([["a", "b", "c"], ["x", "y", "zzz"]])
    >>> "zzz|a|b|c|x|y"
    """
    escaped = []
    for i in li:
        if isinstance(i, list):
            for ii in i:
                escaped.append(re.escape(ii))
        else:
            escaped.append(re.escape(i))
    escaped.sort(reverse = True)
    returnstring = "|".join(escaped)
    if capture:
        returnstring = f"({returnstring})"
    return returnstring
