import pytest

@pytest.mark.dummy
def test_hello_dummy(dummy_str: str):
    assert dummy_str is not None, "dummy_str cannot be None"
    assert isinstance(dummy_str, str), "dummy_str must be of type str"
    
    print(f"Hello, {dummy_str}")
