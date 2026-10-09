"""Tests for textdiff.unified module."""

import pytest

from textdiff.unified import unified_diff


def test_unified_diff_negative_context_raises():
    """unified_diff raises ValueError when context is negative."""
    with pytest.raises(ValueError, match="context must be non-negative"):
        unified_diff(["a"], ["b"], context=-1)
