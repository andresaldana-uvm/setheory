# _developer-tools/tests/test_relations.py
from setheory.api import Set


def test_subset():
    universe = {1, 2, 3}
    odds = Set(universe, lambda x: x % 2 == 1)
    all_numbers = Set(universe, lambda x: True)

    assert odds <= all_numbers


def test_proper_subset():
    universe = {1, 2, 3}
    odds = Set(universe, lambda x: x % 2 == 1)
    all_numbers = Set(universe, lambda x: True)

    assert odds < all_numbers


def test_equal_sets():
    universe = {1, 2, 3}
    first = Set(universe, lambda x: x in {1, 2})
    second = Set(universe, lambda x: x <= 2)

    assert first == second


def test_unequal_sets():
    universe = {1, 2, 3}
    first = Set(universe, lambda x: x in {1, 2})
    second = Set(universe, lambda x: x % 2 == 1)

    assert first != second


def test_equal_sets_need_not_use_same_predicate():
    universe = {1, 2, 3}
    first = Set(universe, lambda x: x in {1, 2})
    second = Set(universe, lambda x: x <= 2)

    assert first == second
