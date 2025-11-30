import math

def log_scale(data, base):
    result = []
    for n in data:
        result.append(math.log(n, base))
    return result
