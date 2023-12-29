from __future__ import annotations

import pytest
from pytest import fixture

@fixture
def test_lst1() -> list:
    return ["test1", "test2", "test3"]


@fixture
def test_lst2() -> list:
    return ["test4", 5, "test6"]
