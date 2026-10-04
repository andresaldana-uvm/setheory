# _developer-tools/tests/test_construction.py
from setheory.api import Set


def test_set_creation():
    universe = {1, 2, 3}
    even = Set(universe, lambda x: x % 2 == 0)

    assert even.universe is universe
    assert even.predicate(2)
    assert not even.predicate(1)


def test_membership():
    universe = {1, 2, 3}
    odd = Set(universe, lambda x: x % 2 == 1)

    assert 1 in odd
    assert 3 in odd
    assert 2 not in odd


def test_membership_requires_element_in_universe():
    universe = {1, 2, 3}
    even = Set(universe, lambda x: x % 2 == 0)

    assert 5 not in even


def test_elements():
    universe = {1, 2, 3, 4}
    even = Set(universe, lambda x: x % 2 == 0)

    assert even.elements == {2, 4}
