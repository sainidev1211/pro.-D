class Solution(object):
    def lengthOfLongestSubstring(self, s):
        arr = []
        longest = 0

        for ch in s:
            while ch in arr:
                arr.pop(0)
            arr.append(ch)

            if longest < len(arr) :
                longest = len(arr)

        return longest
