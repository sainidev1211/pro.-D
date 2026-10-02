class Solution:
        def generateParenthesis(self, n: int) -> list[str]:
            S = {''}
            for _ in range(n):
                S = {
                    s[:i] + '()' + s[i:]
                    for s in S
                    for i in range(len(S) + 1)
                }
            return list(S)