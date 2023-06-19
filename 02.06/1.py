def get_neighbor_position(matrix, i, j):
    start_i = 0 if i -1  < 0  else i - 1
    end_i = len(matrix) if i + 2 >= len(matrix) else i + 2
    start_j = 0 if j - 1 < 0 else j - 1
    end_j = len(matrix) if j + 2 >= len(matrix) else j + 2
    return [(i, j)
            for i in range(start_i, end_i)
            for j in range(start_j, end_j) if matrix[i][j] != 'M']


def m_neighbors(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'M':
                for x, y in get_neighbor_position(matrix, i, j):
                    matrix[x][y] += 1


matrix = [
    [ 0, 'M', 0, 'M', 0],
    [ 0,  0, 'M', 0,  0],
    [ 0,  0,  0,  0,  0],
    ['M', 'M', 0, 0,  0],
    [ 0,  0, 'M', 0,  0]
]


def print_matrix(matrix):
    for row in matrix:
        print(*row, end = '')
        print()


print_matrix(matrix)
m_neighbors(matrix)
print()
print()
print_matrix(matrix)