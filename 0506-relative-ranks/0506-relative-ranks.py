class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        arr = score[:]
        arr.sort(reverse=True)
        ans = []

        for s in score:
            for i in range(len(arr)):
                if s == arr[i]:
                    if i == 0:
                        ans.append("Gold Medal")
                    elif i == 1:
                        ans.append("Silver Medal")
                    elif i == 2:
                        ans.append("Bronze Medal")
                    else:
                        ans.append(str(i + 1))
                    break

        return ans