from mathematica.algebra.matrices import add_matrices, sub_matrices

import pytest

import numpy

def test_add_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b = [
        [4, 5, 6],
        [1, 2, 3]
    ]
    result = add_matrices(a, b)
    assert result == [[5, 7, 9], [5, 7, 9]]



def test_add_matrices_with_different_ocunt_of_rows():
    a = numpy.array([[1, 2], [3, 4], [5, 6]])
    b = numpy.array([[1, 2], [4, 5]])

    with pytest.raises(ValueError) as e:
        result = add_matrices(a, b)

def test_add_matrices_with_different_ocunt_of_cols():
    a = numpy.array([[1, 2], [3, 4]])
    b = numpy.array([[1, 2, 3], [4, 5, 6]])

    with pytest.raises(ValueError) as e:
        result = add_matrices(a, b)

