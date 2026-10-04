# setheory/_core/set.py
from collections.abc import Callable


class Set:
    """
    Represents the set A = {x in U | P(x)}.
    """

    def __init__(self, U, P: Callable):
        self.U = U
        self.P = P

    def __contains__(self, x):
        return x in self.U and self.P(x)

    @property
    def elements(self) -> set:
        """
        Returns A = {x in U | P(x)}.
        """
        return {x for x in self.U if self.P(x)}

    # set operations
    def __and__(self, B):
        """
        Returns A & B = {x in U | P(x) and Q(x)}.
        """
        self._validate(B)
        return Set(self.U, lambda x: self.P(x) and B.P(x))

    def __or__(self, B):
        """
        Returns A | B = {x in U | P(x) or Q(x)}.
        """
        self._validate(B)
        return Set(self.U, lambda x: self.P(x) or B.P(x))

    def __sub__(self, B):
        """
        Returns A - B = {x in U | P(x) and not Q(x)}.
        """
        self._validate(B)
        return Set(self.U, lambda x: self.P(x) and not B.P(x))

    def __xor__(self, B):
        """
        Returns A ^ B = {x in U | P(x) xor Q(x)}.
        """
        self._validate(B)
        return Set(self.U, lambda x: self.P(x) != B.P(x))

    def __invert__(self):
        """
        Returns the complement of A: {x in U | not P(x)}.
        """
        return Set(self.U, lambda x: not self.P(x))

    # set-relations
    def __le__(self, B):
        """
        Tests whether A is a subset of B: A <= B.
        """
        self._validate(B)
        return self.elements <= B.elements

    def __lt__(self, B):
        """
        Tests whether A is a proper subset of B: A < B.
        """
        self._validate(B)
        return self.elements < B.elements

    def __eq__(self, B):
        """
        Tests whether A = B.
        """
        if not isinstance(B, Set):
            return NotImplemented
        self._validate(B)
        return self.elements == B.elements

    # private methods
    def _validate(self, B):
        if self.U is not B.U:
            raise ValueError("Sets must be the same universe.")

    def __repr__(self):
        return f"Set({self.elements!r})"

    def __str__(self):
        return str(self.elements)
