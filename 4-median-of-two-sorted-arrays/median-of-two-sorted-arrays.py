class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        
        # Extend or append the elements from both sorted arrays
        nums.extend(nums1)
        nums.extend(nums2)
        
        # Sort the combined list
        nums.sort()
        
        length = len(nums)
        mid = length // 2
       
        if length % 2 == 0:
            return float(nums[mid - 1] + nums[mid]) / 2.0
        else:
            
            return float(nums[mid])