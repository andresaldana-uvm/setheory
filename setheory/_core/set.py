# setheory/_core/set.py
from collections.abc import Callable


class Set:
    """Representa un conjunto definido por un predicado sobre un universo.

    Un conjunto se define como ``A = {x in U | P(x)}``, donde ``U`` es el
    universo y ``P`` es un predicado que determina la pertenencia de los
    elementos.

    Notes
    -----
    Cada instancia de ``Set`` está asociada a un objeto universo específico.
    Las operaciones y relaciones entre conjuntos requieren que los operandos
    compartan ese mismo objeto universo.
    """

    def __init__(
        self,
        universe,
        predicate: Callable[[object], bool],
    ):
        """Inicializa un conjunto definido por un predicado.

        Parameters
        ----------
        universe : iterable
            Universo sobre el que se define el conjunto.
        predicate : Callable[[object], bool]
            Predicado que determina si un elemento pertenece al conjunto.

        Examples
        --------
        >>> universe = {1, 2, 3}
        >>> even = Set(universe, lambda x: x % 2 == 0)
        >>> 2 in even
        True
        """
        self.universe = universe
        self.predicate = predicate

    def __contains__(self, x):
        """Determina si un elemento pertenece al conjunto.

        Un elemento pertenece al conjunto si pertenece al universo y el
        predicado evalúa como verdadero para dicho elemento.

        Parameters
        ----------
        x : object
            Elemento cuya pertenencia se desea comprobar.

        Returns
        -------
        bool
            ``True`` si ``x`` pertenece al conjunto y ``False`` en caso
            contrario.

        Examples
        --------
        >>> universe = {1, 2, 3}
        >>> odd = Set(universe, lambda x: x % 2 == 1)
        >>> 3 in odd
        True
        >>> 2 in odd
        False
        """
        return x in self.universe and bool(self.predicate(x))

    @property
    def elements(self) -> set:
        """Devuelve los elementos del conjunto.

        Returns
        -------
        set
            Elementos del universo que satisfacen el predicado del conjunto.

        Examples
        --------
        >>> universe = {1, 2, 3, 4}
        >>> even = Set(universe, lambda x: x % 2 == 0)
        >>> even.elements
        {2, 4}
        """
        return {x for x in self.universe if self.predicate(x)}

    # Set operations
    def __and__(self, other):
        """Calcula la intersección con otro conjunto.

        El conjunto resultante se define como
        ``{x in U | P(x) and Q(x)}``.

        Parameters
        ----------
        other : Set
            Conjunto con el que se calcula la intersección.

        Returns
        -------
        Set
            Nuevo conjunto que representa la intersección de ambos conjuntos.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3, 4}
        >>> evens = Set(universe, lambda x: x % 2 == 0)
        >>> multiples_of_three = Set(universe, lambda x: x % 3 == 0)
        >>> (evens & multiples_of_three).elements
        set()
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return Set(
            self.universe,
            lambda x: self.predicate(x) and other.predicate(x),
        )

    def __or__(self, other):
        """Calcula la unión con otro conjunto.

        El conjunto resultante se define como
        ``{x in U | P(x) or Q(x)}``.

        Parameters
        ----------
        other : Set
            Conjunto con el que se calcula la unión.

        Returns
        -------
        Set
            Nuevo conjunto que representa la unión de ambos conjuntos.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3, 4}
        >>> evens = Set(universe, lambda x: x % 2 == 0)
        >>> primes = Set(universe, lambda x: x in {2, 3})
        >>> (evens | primes).elements
        {2, 3, 4}
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return Set(
            self.universe,
            lambda x: self.predicate(x) or other.predicate(x),
        )

    def __sub__(self, other):
        """Calcula la diferencia con otro conjunto.

        El conjunto resultante se define como
        ``{x in U | P(x) and not Q(x)}``.

        Parameters
        ----------
        other : Set
            Conjunto que se desea sustraer.

        Returns
        -------
        Set
            Nuevo conjunto que representa la diferencia entre ambos
            conjuntos.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3, 4}
        >>> evens = Set(universe, lambda x: x % 2 == 0)
        >>> primes = Set(universe, lambda x: x in {2, 3})
        >>> (evens - primes).elements
        {4}
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return Set(
            self.universe,
            lambda x: self.predicate(x) and not other.predicate(x),
        )

    def __xor__(self, other):
        """Calcula la diferencia simétrica con otro conjunto.

        El conjunto resultante se define como
        ``{x in U | P(x) != Q(x)}``.

        Parameters
        ----------
        other : Set
            Conjunto con el que se calcula la diferencia simétrica.

        Returns
        -------
        Set
            Nuevo conjunto que representa la diferencia simétrica de ambos
            conjuntos.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3, 4}
        >>> evens = Set(universe, lambda x: x % 2 == 0)
        >>> primes = Set(universe, lambda x: x in {2, 3})
        >>> (evens ^ primes).elements
        {3, 4}
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return Set(
            self.universe,
            lambda x: self.predicate(x) != other.predicate(x),
        )

    def __invert__(self):
        """Calcula el complemento del conjunto.

        El complemento se define con respecto al universo del conjunto como
        ``{x in U | not P(x)}``.

        Returns
        -------
        Set
            Nuevo conjunto que representa el complemento del conjunto.

        Examples
        --------
        >>> universe = {1, 2, 3, 4}
        >>> evens = Set(universe, lambda x: x % 2 == 0)
        >>> (~evens).elements
        {1, 3}
        """
        return Set(self.universe, lambda x: not self.predicate(x))

    # Set relations
    def __le__(self, other):
        """Determina si el conjunto es subconjunto de otro conjunto.

        Parameters
        ----------
        other : Set
            Conjunto con el que se compara.

        Returns
        -------
        bool
            ``True`` si este conjunto es subconjunto de ``other`` y ``False``
            en caso contrario.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3}
        >>> odds = Set(universe, lambda x: x % 2 == 1)
        >>> all_numbers = Set(universe, lambda x: True)
        >>> odds <= all_numbers
        True
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return self.elements <= other.elements

    def __lt__(self, other):
        """Determina si el conjunto es subconjunto propio de otro conjunto.

        Parameters
        ----------
        other : Set
            Conjunto con el que se compara.

        Returns
        -------
        bool
            ``True`` si este conjunto es subconjunto propio de ``other`` y
            ``False`` en caso contrario.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3}
        >>> odds = Set(universe, lambda x: x % 2 == 1)
        >>> all_numbers = Set(universe, lambda x: True)
        >>> odds < all_numbers
        True
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return self.elements < other.elements

    def __eq__(self, other):
        """Determina si dos conjuntos contienen los mismos elementos.

        La comparación requiere que ambos conjuntos estén definidos sobre el
        mismo objeto universo.

        Parameters
        ----------
        other : Set
            Conjunto con el que se compara.

        Returns
        -------
        bool
            ``True`` si ambos conjuntos contienen los mismos elementos y
            ``False`` en caso contrario.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Examples
        --------
        >>> universe = {1, 2, 3}
        >>> a = Set(universe, lambda x: x in {1, 2})
        >>> b = Set(universe, lambda x: x % 2 == 1)
        >>> a == b
        False
        """
        if not isinstance(other, Set):
            return NotImplemented

        self._validate(other)
        return self.elements == other.elements

    # Private methods
    def _validate(self, other):
        """Valida que otro conjunto comparta el mismo universo.

        Parameters
        ----------
        other : Set
            Conjunto que se desea validar.

        Raises
        ------
        ValueError
            Si los conjuntos no comparten el mismo universo.

        Notes
        -----
        La comprobación se realiza mediante identidad, no mediante igualdad,
        porque el universo se considera un único objeto que define el dominio
        del conjunto.
        """
        if self.universe is not other.universe:
            raise ValueError("Sets must be defined over the same universe.")

    def __repr__(self):
        """Devuelve la representación oficial del conjunto.

        Returns
        -------
        str
            Representación del conjunto basada en sus elementos actuales.
        """
        return f"Set({self.elements!r})"

    def __str__(self):
        """Devuelve la representación informal del conjunto.

        Returns
        -------
        str
            Representación de los elementos del conjunto.
        """
        return str(self.elements)
