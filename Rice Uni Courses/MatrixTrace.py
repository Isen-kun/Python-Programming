NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)

# print the matrix
for row in my_matrix:
    print(row)


def trace(matrix):
    Sum = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if i == j:
                Sum += matrix[i][j]
    print(Sum)


trace(my_matrix)
