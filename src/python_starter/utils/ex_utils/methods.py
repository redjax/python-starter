from __future__ import annotations

def join_lists(lst1: list = None, lst2: list = None) -> list:
    assert lst1 is not None, "lst1 cannot be None"
    assert isinstance(lst1, list), "lst1 must be of type list"
    assert lst2 is not None, "lst2 cannot be None"
    assert isinstance(lst2, list), "lst2 must be of type list"

    joined = lst1 + lst2

    return joined
