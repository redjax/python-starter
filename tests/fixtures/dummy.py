from __future__ import annotations

from pytest import fixture

@fixture
def dummy_hello_str() -> str:
    return "world"
