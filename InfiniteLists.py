#!/usr/bin/env python3

from random import random as rand

class InfiniteList:

    @staticmethod
    def _repeat_gen(x):
        while True:
            yield x

    @staticmethod
    def _pattern_gen(start, pattern):
        n = start
        i = 1

        while True:
            yield n
            n = pattern(n) if len(pattern.__code__.co_varnames) == 1 else pattern(i, n)
            i += 1

    @staticmethod
    def _map_gen(g, g_args: tuple, pattern):
        for x in g(*g_args):
            yield pattern(x)

    @staticmethod
    def _filter_gen(g, g_args: tuple, rule):
        for x in g(*g_args):
            if rule(x):
                yield x

    @staticmethod
    def _combine_gen(g1, g1_args: tuple, g2, g2_args: tuple, combinator):
        for a, b in zip(g1(*g1_args), g2(*g2_args)):
            yield combinator(a, b)

    @staticmethod
    def repeat(number: int = 0):
        return InfiniteList(InfiniteList._repeat_gen, (number,))

    @staticmethod
    def pattern(start: int = 0, pattern = lambda x: x):
        return InfiniteList(InfiniteList._pattern_gen, (start, pattern))

    def __init__(self, igen, igen_args):
        self.igen = igen
        self.igen_args = igen_args

    def __repr__(self) -> str:
        return f"{str(self[:10])[:-1]}, ...]"

    def __iter__(self):
        yield from self.igen(*self.igen_args)

    def combine_with_list(self, other, combinator):
        combine_igen_args = (self.igen, self.igen_args, other.igen, other.igen_args, combinator)
        return InfiniteList(InfiniteList._combine_gen, combine_igen_args)

    def combine_with_scalar(self, scalar, combinator):
        combine_igen_args = (self.igen, self.igen_args, InfiniteList._repeat_gen, (scalar,), combinator)
        return InfiniteList(InfiniteList._combine_gen, combine_igen_args)

    def map(self, pattern):
        map_igen_args = (self.igen, self.igen_args, pattern)
        return InfiniteList(InfiniteList._map_gen, map_igen_args)

    def filter(self, rule):
        map_igen_args = (self.igen, self.igen_args, rule)
        return InfiniteList(InfiniteList._filter_gen, map_igen_args)

    def __len__(self) -> float:
        raise ValueError("List has infinite length.")

    def __add__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x + y))

        return self.combine_with_scalar(other, (lambda x, y: x + y))

    def __sub__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x - y))

        return self.combine_with_scalar(other, (lambda x, y: x - y))

    def __mul__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x * y))

        return self.combine_with_scalar(other, (lambda x, y: x * y))

    def __div__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x / y))

        return self.combine_with_scalar(other, (lambda x, y: x / y))

    def __floordiv__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x // y))

        return self.combine_with_scalar(other, (lambda x, y: x // y))

    def __mod__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x % y))

        return self.combine_with_scalar(other, (lambda x, y: x % y))

    def __pow__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x ** y))

        return self.combine_with_scalar(other, (lambda x, y: x ** y))

    def __and__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x & y))

        return self.combine_with_scalar(other, (lambda x, y: x & y))

    def __or__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x | y))

        return self.combine_with_scalar(other, (lambda x, y: x | y))

    def __xor__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x ^ y))

        return self.combine_with_scalar(other, (lambda x, y: x ^ y))

    def __lshift__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x << y))

        return self.combine_with_scalar(other, (lambda x, y: x << y))

    def __rshift__(self, other):
        if isinstance(other, InfiniteList):
            return self.combine_with_list(other, (lambda x, y: x >> y))

        return self.combine_with_scalar(other, (lambda x, y: x >> y))

    # Less than
    def __lt__(self, other) -> bool:
        for a, b in zip(self, other):
            if a == b:
                continue

            return a < b

    # Less than or equal to
    def __le__(self, other) -> bool:
        for a, b in zip(self, other):
            return a <= b

    # Not equal to
    def __ne__(self, other) -> bool:
        for a, b in zip(self, other):
            if a != b:
                continue

            return False

    # Negative sing in front of list
    def __neg__(self):
        return self.map(lambda x: -x)

    def __abs__(self):
        return self.map(lambda x: abs(x))

    # Bitwise not (~)
    def __invert__(self):
        return self.map(lambda x: ~x)

    def __getitem__(self, index):
        if isinstance(index, slice):
            output = []
            r = range(index.start or 0, index.stop or (-1), abs(index.step or 1))

            for i, item in enumerate(self):
                if i in r:
                    output.append(item)
                if i >= index.stop:
                    break

            if (index.step or 1) < 0:
                output.reverse()

            return output
        return next((x for i, x in enumerate(self) if i == index))

    # Does nothing because it's an infinite list; you're never going to reach the end
    def append(self, _):
        pass

    def extend(self, _):
        pass

    def clear(self) -> list:
        return []

    def copy(self):
        return InfiniteList(self.igen, self.igen_args)

    def index(self, item) -> int:
        for i, x in enumerate(self):
            if x == item:
                return i

    def random(self):
        for i, x in enumerate(self):
            if rand() <= 0.0000001:
                return x
