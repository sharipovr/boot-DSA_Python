def insertion_sort(nums):
    i = 1
    j = 1
    while i < len(nums):
        while (j-1) >= 0 and nums[j-1] > nums[j]:
          nums[j-1], nums[j] = nums[j], nums[j-1]
          j -= 1

        i += 1
        j = i
    return nums