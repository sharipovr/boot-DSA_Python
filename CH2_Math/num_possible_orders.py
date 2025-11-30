def num_possible_orders(num_posts):
    result = 1
    if num_posts < 1:
        return None
    for n in range(num_posts, 1, -1):
        result *= n

    return result
