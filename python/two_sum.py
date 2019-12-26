
from collections import Counter

class Solution:

    def twoSum(self, arr, k):
        counters = Counter(arr)
        for n in arr:
            x = k - n
            count = counters.get(x, 0)
            if (count == 1 and x != n) or (count > 1):
                print(n, x)
                return True
        print(counters)
        return False

s = Solution()
print(s.twoSum([100, 43, 1, 70, -80, 4, 5, 1, 1, 4, 0], -80))
