def find_minimum(nums):
  min = float("inf")
  if len(nums) == 0:
    return None
  
  for num in nums:
    if num < min:
      min = num
      
  return min
  