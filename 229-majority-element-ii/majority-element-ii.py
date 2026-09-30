from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        counts = Counter(nums)
        
        return [num for num, count in counts.items() if count > n // 3]