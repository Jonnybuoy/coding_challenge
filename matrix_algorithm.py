def matrix_max_min_value(matrix):
    m, n = len(matrix), len(matrix[0])
    result = []

    for i in range(m):
        max_row = max(matrix[i])
        min_col = min([matrix[j][i] for j in range(n)])
        if max_row == min_col:
            result.append(max_row)
    
    print(result)

    return result


if __name__ == '__main__':
    matrix = input("Enter your matrix values: ")
    matrix_max_min_value(matrix)
