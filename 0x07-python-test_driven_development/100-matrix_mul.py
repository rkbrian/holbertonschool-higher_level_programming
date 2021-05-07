#!/usr/bin/python3
"""
This code will calculate the matrix multiplication, how exciting!
I have learned this in college before, but now, time to calculate with code!
No more hand calc!
-- Laughing like an evil scientist --
"""


def matrix_mul(m_a, m_b):
    """matrix_mul: the module."""

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if isinstance(m_a, type([[1, 1], [1, 1]])) is False:
        raise TypeError("m_a must be a list of lists")
    if isinstance(m_b, type([[1, 1], [1, 1]])) is False:
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for ai in range(len(m_a)):
        for aj in range(len(m_a[ai])):
            if type(m_a[ai][aj]) != int and type(m_a[ai][aj]) != int:
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[ai]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for bi in range(len(m_b)):
        for bj in range(len(m_b[bi])):
            if type(m_b[bi][bj]) != int and type(m_b[bi][bj]) != int:
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[bi]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    """Error messages above, multiplication below"""
    c = [[]]
    ai = len(m_a)
    ajbi = len(m_a[0])
    bj = len(m_b[0])
    for i in range(ai):
        for j in range(bj):
            for rowcol in range(ajbi):
                c[i][j] += m_a[i][rowcol] * m_b[rowcol][j]
    return c
