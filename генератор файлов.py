import random


def create_mirror_matrix(n):
    matrix = [[random.randint(0, 4) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i] = matrix[i][j]

    return matrix


def write_matrix_to_file(matrix):
    with open('matrix.txt', 'w') as file:
        for row in matrix:
            file.write(' '.join(str(elem) for elem in row))
            file.write(' \n')


n = int(input("Введите число n: "))
matrix = create_mirror_matrix(n)
write_matrix_to_file(matrix)
