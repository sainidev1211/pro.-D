class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        nums.sort()
        result = []
        count = 1  

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Check if the previous group exceeded n // 3
                if count > n // 3:
                    result.append(nums[i - 1])
                count = 1  
        if count > n // 3:
            result.append(nums[-1])

        return result