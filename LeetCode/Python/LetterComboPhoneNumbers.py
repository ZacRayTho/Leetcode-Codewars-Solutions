# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # assign 2-9 to an array of corresponding chars
        # ex: 2 = [a, b, c]
        # this is a backtracking problem with a recursive solution
        result = []
        num = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k', 'l'],['m', 'n', 'o'],['p', 'q', 'r', 's'],['t', 'u', 'v'],['w','x','y','z']]
        
        # so ex: digits == "23"
        # backtrack(0, "") called
        # misses IF statement because "" length != "23" length
        # FOR LOOP: FOR character in [A,B,C] because thats the corresponding array for the number 2
        #   backtrack(1, "A") called
        #   misses IF, because "A" length != "23" length
        #   FOR LOOP: FOR character in [D,E,F] because thats the corresponding array for the number 3
        #       backtrack(2, "AD") called
        #       IF statement hits because "AD" length == "23" length
        #           result array gets "AD" appended
        #           result = ["AD"]
        #       back in for loop
        #       backtrack(2, "AE") called
        #       IF statement hits because "AE" length == "23" length
        #           result = ["AD", "AE"]
        # This makes sense to me so im going to stop explaining for myself

        def backtrack(index, curString):
            if len(curString) == len(digits):
                result.append(curString)
                return

            for c in num[int(digits[index]) - 2]:
                backtrack(index + 1, curString + c)

        # only call backtrack function if the digits string isn't empty
        if digits:
            backtrack(0, "")

        # if the digits string is empty return the empty result array
        return result


