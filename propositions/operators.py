# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *

def to_not_and_or(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'``, ``'&'``, and ``'|'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'``, ``'&'``, and
        ``'|'``.
    """
    # Task 3.5
    mapa = {'+': Formula.parse('((p|q)&~(p&q))'), '->': Formula.parse('(~p|q)'), '<->': Formula.parse('((p&q)|(~p&~q))'), '-|' : Formula.parse('~(p|q)'), '-&' : Formula.parse('~(p&q)'), 'T': Formula.parse('(p|~p)'), 'F':Formula.parse('(p&~p)')}
    return formula.substitute_operators(mapa)

def to_not_and(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'`` and ``'&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'`` and ``'&'``.
    """
    # Task 3.6a
    a = to_not_and_or(formula)
    mapa = {'|': Formula.parse('~(~p&~q)')}
    return a.substitute_operators(mapa)

def to_nand(formula: Formula) -> Formula:
    a = to_not_and(formula)

    p = Formula('p')
    q = Formula('q')

    not_p = Formula('-&', p, p)
    pnq = Formula('-&', p, q)
    and_pq = Formula('-&', pnq, pnq)

    mapa = {
        '~': not_p,
        '&': and_pq
    }
    return a.substitute_operators(mapa)


def to_implies_not(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'~'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'~'``.
    """
    # Task 3.6c
    a = to_nand(formula)
    mapa = {'-&':Formula.parse('(p->~q)')}
    return a.substitute_operators(mapa)

def to_implies_false(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'F'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'F'``.
    """
    a = to_implies_not(formula)
    mapa = {'~': Formula.parse('(p->F)')}
    return a.substitute_operators(mapa)
