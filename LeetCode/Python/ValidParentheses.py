# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        # loop through string
        # keep memory of all open parantheses
        # check that memory, when encountering closing paratheses for matching paranthese
        open = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                open.append(char)
            elif char == ")" and len(open) != 0 and open[len(open) - 1] == "(":
                open.pop()
            elif char == "}" and len(open) != 0 and open[len(open) - 1] == "{":
                open.pop()
            elif char == "]" and len(open) != 0 and open[len(open) - 1] == "[":
                open.pop()
            else: 
                return False

        if len(open) == 0:
            return True