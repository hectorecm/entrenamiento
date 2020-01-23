class Solution:
  def sortColors(self, nums):
    counters = dict.fromkeys(nums, 0)
    result = []
    for n in nums:
      counters[n] += 1
    
    for color, times in counters.items():
      result += [color] * times
    return result

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

nums = Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]