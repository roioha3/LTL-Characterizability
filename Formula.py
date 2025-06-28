from typing import Union

class Formula:
    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Formula) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


# Atomic proposition or literal
class Atom(Formula):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


# Logical Connectives
class Not(Formula):
    def __init__(self, inner: Formula):
        self.inner = inner

    def __str__(self):
        return f"¬({self.inner})"


class And(Formula):
    def __init__(self, left: Formula, right: Formula):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} ∧ {self.right})"


class Or(Formula):
    def __init__(self, left: Formula, right: Formula):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} ∨ {self.right})"


# Temporal Operators
class Global(Formula):
    def __init__(self, inner: Formula):
        self.inner = inner

    def __str__(self):
        return f"G({self.inner})"


class Future(Formula):
    def __init__(self, inner: Formula):
        self.inner = inner

    def __str__(self):
        return f"F({self.inner})"


class StrictFuture(Formula):
    def __init__(self, inner: Formula):
        self.inner = inner

    def __str__(self):
        return f"F⁺({self.inner})"


class Until(Formula):
    def __init__(self, left: Formula, right: Formula):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} U {self.right})"


class Next(Formula):
    def __init__(self, inner: Formula):
        self.inner = inner

    def __str__(self):
        return f"X({self.inner})"
