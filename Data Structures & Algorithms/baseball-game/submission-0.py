class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res_stack = []

        for value in operations:
            if value == "+":
                res_stack.append(res_stack[-1] + res_stack[-2])
            elif value == "D":
                res_stack.append(res_stack[-1]*2)
            elif value == "C":
                res_stack.pop()
            else:
                res_stack.append(int(value))

        return sum(res_stack)