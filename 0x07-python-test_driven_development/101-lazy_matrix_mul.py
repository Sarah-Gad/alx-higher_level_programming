#!/usr/bin/python3
"""
This module multiplies wo matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    the methos that multiplies two matrix that is given
    Args:
        m_a: input first mat
        m_b: input second mat
    """
    return numpy.matmul(m_a, m_b)
