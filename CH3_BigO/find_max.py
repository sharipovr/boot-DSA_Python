def find_max(nums):
  max = float("-inf")
  for n in nums:
    if n > max:
      max = n

  return max
