class Solution:
    def decodeString(self, s):

        value = []      
        string = []   

        num = 0
        temp = ""

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                value.append(num)
                string.append(temp)
                num = 0
                temp = ""

            elif ch == "]":
                n = value.pop()
                prev = string.pop()
                temp = prev + (temp * n)

            else:
                temp += ch

        return temp