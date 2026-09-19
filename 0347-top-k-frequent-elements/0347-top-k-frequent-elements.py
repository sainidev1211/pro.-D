class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        bucket = [[] for i in range(len(nums) + 1)]

        for i in count:
            bucket[count[i]].append(i)

        res = []

        for i in range(len(nums), 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res