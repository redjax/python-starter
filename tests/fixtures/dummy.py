from pytest import fixture

@fixture
def dummy_str() -> str:
    return "dummy"