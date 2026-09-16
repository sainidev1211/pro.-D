class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        self.stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                self.stack.append(int(tokens[i]))
            else:
                e1 = self.stack.pop()
                e2 = self.stack.pop()

                if tokens[i] == "+":
                    M = e2 + e1
                elif tokens[i] == "-":
                    M = e2 - e1
                elif tokens[i] == "*":
                    M = e2 * e1
                else:
                    M = int(float(e2) / e1)

                self.stack.append(M)

        return self.stack[-1]