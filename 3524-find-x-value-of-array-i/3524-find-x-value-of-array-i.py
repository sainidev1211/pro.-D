class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            mod = num % k
            new_dp = [0] * k

            new_dp[mod] += 1

            for old_r in range(k):
                new_r = (old_r * mod) % k
                new_dp[new_r] += dp[old_r]
            
            for r in range(k):
                ans[r] += new_dp[r]
            
            dp = new_dp
        
        return ans