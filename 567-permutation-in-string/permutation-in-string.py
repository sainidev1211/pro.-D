class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1)

        for i in range(len(s2) - n + 1):      # check every window
            window = s2[i:i+n]                # substring of same length

            # compare sorted characters
            if sorted(window) == sorted(s1):
                return True

        return False