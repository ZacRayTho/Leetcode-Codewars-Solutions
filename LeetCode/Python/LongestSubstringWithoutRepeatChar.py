# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # loop through all letter of given string
        # have 2 pointers, one for start of substring, other for end
        # have len of chars between and including pointers
        # keep moving end pointer forward until hitting repeated character
        # upon hitting it, move start pointer one index past the first appearance of repeated character
        # then start moving end pointer, starting from new index
        chars = {}
        # chars dict keeps track of all indices that that the end pointer has hit
        # the key will be the char, and the value will be the last touched index
        # so i know where to start if hitting repeated char, 
        begin = 0
        # begin is the start pointer
        high = 0
        # high will keep length of longest substring
        for end in range(len(s)):
            # print("round", end, "high", high, "start=", begin, "chars dict", chars)
            # loop through the length, to keep track of index
            if s[end] in chars and chars[s[end]] >= begin:
                # if the character at current index is in the dict
                # that means ive seen it before
                
                # check if the current index is greater or equal the the start pointer
                begin = chars[s[end]] + 1
                # if so, move start pointer past the last known index of current char
            else:
                # if the character is new
                if end - begin + 1 > high:
                    # if the length of start pointer to end pointer is more than the current longest substring, replace it
                    high = end - begin + 1
            # update the current index's key in the dictionary with the current index as value
            chars[s[end]] = end
                
        # return the length of longest substring
        return high




