def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return nums
    m = n // 2
    return merge(merge_sort(nums[0:m]),
                  merge_sort(nums[m:n]))


def merge(first, second):
    final = []
    i, j = 0, 0
    k, l = len(first), len(second)
    not_end = True
    while not_end:
      if first[i] <= second[j]:
          final.append(first[i])
          i += 1
      else:
          final.append(second[j])
          j += 1 
      if i == k or j == l:
          not_end = False

    while j < l:
        final.append(second[j])
        j += 1
    while i < k:
        final.append(first[i])
        i += 1    
    
    return final