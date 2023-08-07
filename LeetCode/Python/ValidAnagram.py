class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = dict()
        for char in s:
            check[char] = check.get(char, 0) + 1

        check2 = dict()
        for char in t:
            check2[char] = check2.get(char, 0) + 1
        
        if check == check2:
            return True
        return False

        
