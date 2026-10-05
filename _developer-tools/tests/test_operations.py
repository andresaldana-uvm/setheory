# _developer-tools/tests/test_operations.py
from setheory.api import Set


def test_intersection():
    universe = {1, 2, 3, 4}
    evens = Set(universe, lambda x: x % 2 == 0)
    multiples_of_three = Set(universe, lambda x: x % 3 == 0)

    result = evens & multiples_of_three

    assert result.elements == set()


def test_union():
    universe = {1, 2, 3, 4}
    evens = Set(universe, lambda x: x % 2 == 0)
    primes = Set(universe, lambda x: x in {2, 3})

    result = evens | primes

    assert result.elements == {2, 3, 4}


def test_difference():
    universe = {1, 2, 3, 4}
    evens = Set(universe, lambda x: x % 2 == 0)
    primes = Set(universe, lambda x: x in {2, 3})

    result = evens - primes

    assert result.elements == {4}


def test_symmetric_difference():
    universe = {1, 2, 3, 4}
    evens = Set(universe, lambda x: x % 2 == 0)
    primes = Set(universe, lambda x: x in {2, 3})

    result = evens ^ primes

    assert result.elements == {3, 4}


def test_complement():
    universe = {1, 2, 3, 4}
    evens = Set(universe, lambda x: x % 2 == 0)

    result = ~evens

    assert result.elements == {1, 3}


def test_operations_preserve_universe():
    universe = {1, 2, 3}
    evens = Set(universe, lambda x: x % 2 == 0)
    odds = Set(universe, lambda x: x % 2 == 1)

    assert (evens & odds).universe is universe
    assert (evens | odds).universe is universe
    assert (evens - odds).universe is universe
    assert (evens ^ odds).universe is universe
    assert (~evens).universe is universe
