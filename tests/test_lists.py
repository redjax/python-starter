from __future__ import annotations

import pytest
from pytest import mark
from python_starter.utils.ex_utils import join_lists

@mark.lists
@mark.xfail
def test_xfail_list1(test_lst1: list):
    assert test_lst1 is not None, "test_lst1 cannot be None"
    assert not isinstance(
        test_lst1, list
    ), f"test_lst1 must be of type list, got: {type(test_lst1)}"


@mark.lists
@mark.xfail
def test_xfail_list2(test_lst2: bool):
    assert test_lst2 is not None, "test_lst2 cannot be None"
    assert not isinstance(
        test_lst2, list
    ), f"test_lst2 must be of type list, got: {type(test_lst2)}"


@mark.lists
def test_xpass_list1(test_lst1: list):
    assert test_lst1 is not None, "test_lst1 cannot be None"
    assert isinstance(
        test_lst1, list
    ), f"test_lst1 must be of type list, got: {type(test_lst1)}"


@mark.lists
def test_xpass_list2(test_lst2: list):
    assert test_lst2 is not None, "test_lst2 cannot be None"
    assert isinstance(
        test_lst2, list
    ), f"test_lst2 must be of type list, got: {type(test_lst2)}"


@mark.lists
def test_join_lists(test_lst1: list, test_lst2: list):
    assert test_lst1 is not None, "test_lst1 cannot be None"
    assert isinstance(
        test_lst1, list
    ), f"test_lst1 must be of type list, got: {type(test_lst1)}"
    assert test_lst2 is not None, "test_lst2 cannot be None"
    assert isinstance(
        test_lst2, list
    ), f"test_lst2 must be of type list, got: {type(test_lst2)}"

    try:
        joined = join_lists(test_lst1, test_lst2)
    except Exception as exc:
        raise Exception(f"Unhandled exception joining lists. Details: {exc}")

    assert joined is not None, "joined list should not be None"
    assert isinstance(
        joined, list
    ), f"joined list should be of type list, not {type(joined)}"
