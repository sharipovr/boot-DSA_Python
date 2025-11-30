def average_followers(nums):
    if len(nums) == 0:
        return None
    sum = 0
    for x in nums:
        sum += x
    return sum/len(nums)
