class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 1

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                count += 1
                if count > n // 2:
                    return nums[i]
            else:
                count = 1

        return nums[0]