// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {

    // Loops through all the letters in first word
    for (x = 0; x < strs[0].length; x++) {
        // Loop through all the other words
        // So this loop goes through all the first letters of each word
        // and compares to first letter of the first word
        // and if they all are the same first letter it goes onto the second letter and repeats
        for (y = 1; y < strs.length; y++) {
            // compare characters from first word to others
            if (strs[0][x] != strs[y][x]) {
                // if characters don't match return up to most recently match character in all words AKA x variable
                return strs[0].slice(0, x)
            }
            
        }
    }

    return strs[0]
};