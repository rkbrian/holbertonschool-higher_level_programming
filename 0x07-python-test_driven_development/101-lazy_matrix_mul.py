#!/usr/bin/python3
"""I feel I'm lazy to write more documentation..."""


def lazy_matrix_mul(m_a, m_b):
    """matrix_mul: the module."""

    import numpy as np
    a = np.array(m_a)
    b = np.array(m_b)
    return a.dot(b)
