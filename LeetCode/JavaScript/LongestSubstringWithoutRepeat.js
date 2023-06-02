// Given a string s, find the length of the longest substringwithout repeating characters.
// NOT SUBMITTED, Currently this solution passes 986/987 testcases but it exceeds server time limit for the final 2 because of the nested for loops
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let arr = []
    let large = 0
    let current = 0
    for (let y = 0; y < s.length; y++) {
        for (let x = y; x < s.length; x++){
            // console.log(x)
            // console.log(arr)
            // console.log(current,"current")
        if (arr.includes(s[x])) {
            current = 0
            arr = []
        }
        arr.push(s[x])
        current = current + 1
        if (current > large) {
            large = large + 1
        }
        }
        arr = []
        current = 0
    }
    return large
};