class Solution:
    def isValid(self, s: str) -> bool:
        # Initially I was thinking to use a while loop where we append characters to the stack until we reach zero,
        # however this doesn't work because it doesn't ensure the entire string is covered.
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen: # "in" keyowrd used on a dict only searches for keys in a dictionary
                if stack and stack[-1] == closeToOpen[c]: # If the c is a key and the head of the stack is the value associated with 
                                                          # the key, then it must be equivalent 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                