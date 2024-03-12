

def boardCutting(cost_y, cost_x, n, m):
    sorted_cost = sorted([(c, 0) for c in cost_y] + [(c, 1) for c in cost_x], reverse=True)
    
    total_cost = 0
    x_cuts = 1
    y_cuts = 1

    for cost, orientation in sorted_cost:
        if orientation == 0:
            total_cost += cost * x_cuts
            y_cuts += 1
        else:
            total_cost += cost * y_cuts
            x_cuts += 1

    return total_cost % (10 ** 9 + 7)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    cost_y = list(map(int, input().rstrip().split()))

    cost_x = list(map(int, input().rstrip().split()))

    result = boardCutting(cost_y, cost_x, n, m)

    print(result)