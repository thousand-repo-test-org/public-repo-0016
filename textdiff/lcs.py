"""Longest-common-subsequence based line diff."""


def lcs_table(a: list[str], b: list[str]) -> list[list[int]]:
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            if a[i] == b[j]:
                table[i][j] = table[i + 1][j + 1] + 1
            else:
                table[i][j] = max(table[i + 1][j], table[i][j + 1])
    return table


def diff_ops(a: list[str], b: list[str]) -> list[tuple[str, str]]:
    """Returns (op, line) pairs where op is ' ', '-', or '+'."""
    table = lcs_table(a, b)
    ops: list[tuple[str, str]] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            ops.append((" ", a[i]))
            i += 1
            j += 1
        elif table[i + 1][j] >= table[i][j + 1]:
            ops.append(("-", a[i]))
            i += 1
        else:
            ops.append(("+", b[j]))
            j += 1
    ops.extend(("-", line) for line in a[i:])
    ops.extend(("+", line) for line in b[j:])
    return ops
