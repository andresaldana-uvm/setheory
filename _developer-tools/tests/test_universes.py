# _developer-tools/tests/test_universes.py
import pytest

from setheory.api import Set


def test_operations_require_same_universe():
    first_universe = {1, 2, 3}
    second_universe = {1, 2, 3}

    first = Set(first_universe, lambda x: x % 2 == 0)
    second = Set(second_universe, lambda x: x % 2 == 1)

    with pytest.raises(
        ValueError,
        match="Sets must be defined over the same universe.",
    ):
        first & second


def test_equal_universes_are_not_the_same_universe():
    first_universe = {1, 2, 3}
    second_universe = {1, 2, 3}

    assert first_universe == second_universe
    assert first_universe is not second_universe


def test_same_universe_object_is_accepted():
    universe = {1, 2, 3}

    first = Set(universe, lambda x: x % 2 == 0)
    second = Set(universe, lambda x: x % 2 == 1)

    result = first | second

    assert result.elements == universe
