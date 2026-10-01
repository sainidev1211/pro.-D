class Solution:
    def validPalindrome(self, s):
        arr = list(s)

        i, j = 0, len(arr) - 1

        while i < j:
            if arr[i] != arr[j]:

                # delete left
                temp = arr[:]
                temp.pop(i)

                if temp == temp[::-1]:
                    return True

                # delete right
                temp = arr[:]
                temp.pop(j)

                if temp == temp[::-1]:
                    return True

                return False

            i += 1
            j -= 1

        return True