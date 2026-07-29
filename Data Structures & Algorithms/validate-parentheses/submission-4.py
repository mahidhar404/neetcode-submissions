class Solution:
    def isValid(self, s: str) -> bool:
        str_stack = []
        closeToOpen = { '}' : '{', ']' : '[', ')': '('}

        for c in s:
            if c in closeToOpen:
                if str_stack and closeToOpen[c] == str_stack[-1]:
                    str_stack.pop()
                else:
                    return False
            else:
                str_stack.append(c)
        
        return True if not str_stack else False