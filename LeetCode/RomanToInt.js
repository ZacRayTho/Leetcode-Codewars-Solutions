// Convert a given Roman Numeral, convert it to an integer

// Constraints:
// 1 <= s.length <= 15
// s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
// It is guaranteed that s is a valid roman numeral in the range [1, 3999].

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let letters = s.split("")
    let sum = 0;
    for (let x = 0; x < letters.length; x++) {
        switch(letters[x]){
            case "I":
                if (letters[x + 1] == "V") {
                    sum += 4
                    x += 1
                    break;
                }
                else if (letters[x + 1] == "X") {
                    sum += 9
                    x += 1
                    break;
                }
                sum += 1
                break;
            case "V":
                sum += 5
                break;
            case "X":
                if (letters[x + 1] == "L") {
                    sum += 40
                    x += 1
                    break;
                }
                else if (letters[x + 1] == "C") {
                    sum += 90
                    x += 1
                    break;
                }
                sum += 10
                break;
            case "L":
                sum += 50
                break;
            case "C":
                if (letters[x + 1] == "D") {
                    sum += 400
                    x += 1
                    break;
                }
                else if (letters[x + 1] == "M") {
                    sum += 900
                    x += 1
                    break;
                }
                sum += 100
                break;
            case "D":
                sum += 500
                break;
            case "M":
                sum += 1000
                break;
        }
    }
    return sum
};
