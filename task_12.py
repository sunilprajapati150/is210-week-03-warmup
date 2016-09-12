#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a docstring"""
import decimal
import fractions

INTVAL = 1
FLOATVAL = 0.1
DECVAL = decimal.Decimal('0.1')
FRACVAL = fractions.Fraction(1,10)

FRAC_DEC_EQUAL = DECVAL == FRACVAL
DEC_FLOAT_INEQUAL = DECVAL != FLOATVAL
