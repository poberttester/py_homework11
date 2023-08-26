import numpy as np


class Matrix:

    def __init__(self, martix1: list, matrix2: list):
        self.matrix1 = martix1
        self.matrix2 = matrix2

    def __repr__(self):
        return print(f'{self.matrix1, self.matrix2}')

    def summ_matrixs(self) -> list:
        """Метод возвращает сумму двух матриц, созданных с помощью библиотеки numpy"""
        return self.matrix1 + self.matrix2

    def equal_matrixs(self) -> bool:
        """Метод сравнивает две матрицы, созданных с помощью библиотеки numpy"""
        return np.array_equal(self.matrix1, self.matrix2)


if __name__ == '__main__':
    MAT1 = np.array([[1, 3, 4], [11, 21, 31]])
    MAT2 = np.array([[4, 1, 26], [5, -2, 10]])
    exemplar = Matrix(MAT1, MAT2)
    result_matrix = exemplar.summ_matrixs()
    is_equal = exemplar.equal_matrixs()
    print(result_matrix)
    print(is_equal)
