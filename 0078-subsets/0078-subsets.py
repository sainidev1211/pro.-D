class Solution(object):
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            new_subsets = []

            for curr in res:
                new_subsets.append(curr + [num])

            res.extend(new_subsets)

        return res