"""Render diff ops as unified-diff hunks with context."""

from .lcs import diff_ops


def unified_diff(a: list[str], b: list[str], context: int = 3,
                 from_name: str = "a", to_name: str = "b") -> str:
    if context < 0:
        raise ValueError("context must be non-negative")
    ops = diff_ops(a, b)
    if all(op == " " for op, _ in ops):
        return ""

    # Group ops into hunks: runs of changes padded with `context` equal lines.
    hunks: list[list[int]] = []
    current: list[int] = []
    last_change = -(context + 1)
    for idx, (op, _) in enumerate(ops):
        if op != " ":
            if idx - last_change > context * 2 and current:
                hunks.append(current)
                current = []
            start = max(0, idx - context, current[-1] + 1 if current else 0)
            current.extend(range(start, idx + 1))
            last_change = idx
    if current:
        current.extend(range(current[-1] + 1, min(len(ops), current[-1] + 1 + context)))
        hunks.append(current)

    lines = [f"--- {from_name}", f"+++ {to_name}"]
    a_pos = b_pos = 0
    consumed = 0
    for hunk in hunks:
        while consumed < hunk[0]:
            op = ops[consumed][0]
            if op in (" ", "-"):
                a_pos += 1
            if op in (" ", "+"):
                b_pos += 1
            consumed += 1
        a_start, b_start = a_pos + 1, b_pos + 1
        a_count = b_count = 0
        body: list[str] = []
        for idx in hunk:
            op, line = ops[idx]
            body.append(op + line)
            if op in (" ", "-"):
                a_count += 1
                a_pos += 1
            if op in (" ", "+"):
                b_count += 1
                b_pos += 1
            consumed += 1
        lines.append(f"@@ -{a_start},{a_count} +{b_start},{b_count} @@")
        lines.extend(body)
    return "\n".join(lines) + "\n"
