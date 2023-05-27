// Given an integer x, return true if x is a palindrome, and false otherwise.

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let y = x.toString();
  let z = y.split("");
  let a = [];
  for (let char = z.length - 1; char > -1; char--) {
    a.push(z[char]);
  }
  if (a.join("") == y) {
    return true;
  }
  return false;
};
