def selection_sort(nums):
  n = len(nums)
  
  for i in range(n):
    # assuming that current position 'i' is position of minimum
    smaller_idx = i
    
    # searching the real minimum in the right part of array
    for j in range(i + 1, n):
      if nums[j] < nums[smaller_idx]:
        smaller_idx = j
    # swap
    nums[i], nums[smaller_idx] = nums[smaller_idx], nums[i]
  
  return nums