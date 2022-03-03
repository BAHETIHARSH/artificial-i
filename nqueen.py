import json

n = 13
a = [[0 for x in range(n)] for y in range(n)]

b = {}


def is_column_safe(row, col):
    while row >= 0:
        if a[row][col] == 1:
            return 0
        row = row - 1
    return 1


def is_left_diagonal_safe(row, col):
    while row >= 0 and col >= 0:
        if a[row][col] == 1:
            return 0
        row = row - 1
        col = col - 1
    return 1


def is_right_diagonal_safe(row, col):
    while row >= 0 and col < n:
        if a[row][col] == 1:
            return 0
        row = row - 1
        col = col + 1
    return 1


def issafe(row, col):
    if is_column_safe(row, col) == 0:
        return 0
    if is_left_diagonal_safe(row, col) == 0:
        return 0
    if is_right_diagonal_safe(row, col) == 0:
        return 0
    return 1


def check_board(r, c):
    if r >= n:
        # print("Solution doesn't exist")
        return
    p = 0

    while c < n:

        p = issafe(r, c)
        if p == 1:
            a[r][c] = 1
            b.update({r: c})
            break
        c = c + 1
    if p == 1:
        check_board(r + 1, 0)
    else:

        a[r - 1][b.get(r - 1)] = 0
        check_board(r - 1, int(b.get(r - 1)) + 1)


if __name__ == "__main__":
    check_board(0, 0)
    for i in a:
        print(i)
