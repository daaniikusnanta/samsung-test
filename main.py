def matrixRotation(matrix, r, m, n):
    num_layers = min(m, n) // 2
    layer_elems = []
    for l in range(num_layers):
        layer_list = []
        layer_list.extend([matrix[l][i] for i in range(l, n - l)])
        layer_list.extend([matrix[i][n - l - 1] for i in range(l + 1, m - l)])
        layer_list.extend([matrix[m - l - 1][i] for i in range(n - l - 2, l - 1, -1)])
        layer_list.extend([matrix[i][l] for i in range(m - l - 2, l, -1)])
        layer_elems.append(layer_list)

    for l in range(num_layers):
        elems = layer_elems[l]
        num_elems = len(elems)
        idx = r % num_elems

        for i in range(l, n - l):
            matrix[l][i] = elems[idx]
            idx = (idx + 1) % num_elems
        
        for i in range(l + 1, m - l):
            matrix[i][n - l - 1] = elems[idx]
            idx = (idx + 1) % num_elems

        for i in range(n - l - 2, l - 1, -1):
            matrix[m - l - 1][i] = elems[idx]
            idx = (idx + 1) % num_elems

        for i in range(m - l - 2, l, -1):
            matrix[i][l] = elems[idx]
            idx = (idx + 1) % num_elems

    for row in matrix:
        print(' '.join(map(str, row))) 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r, m, n)