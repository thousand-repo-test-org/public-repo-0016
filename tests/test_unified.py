import unittest

from textdiff.unified import unified_diff


class UnifiedDiffContextTest(unittest.TestCase):
    def test_negative_context_rejected(self):
        """A negative context empties every hunk, so the diff would silently
        drop all changes and emit only headers; it must fail loudly instead."""
        with self.assertRaisesRegex(ValueError, "context must be non-negative"):
            unified_diff(["a"], ["b"], context=-1)

    def test_negative_context_rejected_for_identical_inputs(self):
        """Validation happens before diffing, so invalid context is rejected
        even when the inputs are identical and no hunks would be produced."""
        with self.assertRaises(ValueError):
            unified_diff(["a"], ["a"], context=-1)

    def test_zero_context_keeps_changes(self):
        """Zero is the boundary of valid context and must still be accepted
        and emit the changed lines."""
        lines = unified_diff(["a"], ["b"], context=0).splitlines()
        self.assertIn("-a", lines)
        self.assertIn("+b", lines)


if __name__ == "__main__":
    unittest.main()
