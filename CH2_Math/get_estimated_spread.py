def get_estimated_spread(audiences_followers):
    n = len(audiences_followers)
    if n == 0:
        return 0
    total = 0
    for num in audiences_followers:
        total += num
    return total / n * (n ** 1.2)
