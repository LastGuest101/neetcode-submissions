class Solution:
    def isValid(self, s: str) -> bool:
        #pointer on start and at end of string s
        #if the pointers are the same move start to the right by 1 and end by left by 1
        #do until pointers are equal to each other, return true
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
            
                if char == ')' and top != '(':
                    return False
                elif char == ']' and top != '[':
                    return False
                elif char == '}' and top != '{':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
            

        