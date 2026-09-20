class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = nums[:]      # copy the list

        for i in range(len(nums)):
            n.append(nums[i])

        return n