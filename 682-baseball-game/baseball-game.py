class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        s = []

        for i in range(len(operations)):
            if operations[i] not in ["C", "D", "+"]:
                s.append(int(operations[i]))
            elif operations[i] == "C":
                s.pop()
            elif operations[i] == "D":
                s.append(s[-1] * 2)
            elif operations[i] == "+":
                s.append(s[-1] + s[-2])

        total = 0
        for sum in s:
            total +=sum
        return total