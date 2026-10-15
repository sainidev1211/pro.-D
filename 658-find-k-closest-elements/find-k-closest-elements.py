class Solution(object):
    def findClosestElements(self, arr, k, x):
        distance_dict = {}
        for i in range(len(arr)):
            distance_dict[i] = abs(arr[i] - x)
            
        sorted_elements = sorted(distance_dict, key=distance_dict.get)
        
        result = [arr[i] for i in sorted_elements[:k]]
        result.sort()
        return result