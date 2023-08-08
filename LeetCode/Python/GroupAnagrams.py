class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        # Key = CharCount : Value = List of valid anagrams
        for i in strs:
            char = [0] * 26 
            # The above initializes an array with 0 in 26 positions
            # this is to count frequency of alphabetical characters

            for j in i:
                char[ord(j) - 97] += 1
            
            count[str(char)] = count.get(str(char), []) + [i]

        return count.values()

