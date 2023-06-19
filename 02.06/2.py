def rotate_180(matrix):
    result = [
        [0 for _ in range(len(matrix))]
        for _ in range(len(matrix))
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i][len(matrix) - 1 - j] = matrix[len(matrix) - 1 - i][j]

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


rotated = rotate_180(matrix)

print_matrix(rotated)