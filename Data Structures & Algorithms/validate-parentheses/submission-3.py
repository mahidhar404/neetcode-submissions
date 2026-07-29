class Solution:
    def isValid(self, s: str) -> bool:
        para_stack = []

        for char in s:
            if char in ['(', '[', "{"]:
                para_stack.append(char)
            elif char == ")":
                if len(para_stack) !=0 and para_stack[-1] == "(":
                    para_stack.pop()
                else: return False
            elif char == "]":
                if len(para_stack) !=0 and para_stack[-1] == "[":
                    para_stack.pop()
                else: return False
            elif char == "}":
                if len(para_stack) !=0 and para_stack[-1] == "{":
                    para_stack.pop()
                else: return False
            else:
                continue
        
        if len(para_stack) == 0:
            return True
        
        return False