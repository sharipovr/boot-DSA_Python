def exponential_growth(n, factor, days):
    result = [n]
    for i in range(1, days+1):
        result.append(result[i - 1] * factor)

    return result
