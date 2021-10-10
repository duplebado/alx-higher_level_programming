#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
        Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
        Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
        Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not any(isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")

    if not any(isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    row_size_A = len(m_a[0])
    row_size_B = len(m_b[0])

    column_A = row_size_A

    result = []

    for i, row in enumerate(m_a):
        if row == []:
            raise ValueError("m_a can't be empty")

        row_result = []

        for k in range(len(row)):
            if (k == row_size_B):
                break

            unit_cell = 0

            for j in (range(len(m_b))):
                if m_b[j] == []:
                    raise ValueError("m_b can't be empty")

                if type(m_a[i][j]) not in [int, float]:
                    err = "m_a should contain only integers or floats"
                    raise TypeError(err)

                if type(m_b[j][k]) not in [int, float]:
                    err = "m_b should contain only integers or floats"
                    raise TypeError(err)

                if len(row) != row_size_A:
                    raise TypeError("each row of m_a must be of the same size")

                if len(m_b[j]) != row_size_B:
                    raise TypeError("each row of m_b must be of the same size")

                if column_A != len(m_b):
                    raise ValueError("m_a and m_b can't be multiplied")

                unit_cell += m_a[i][j] * m_b[j][k]

            row_result.append(unit_cell)

        result.append(row_result)

    return result
