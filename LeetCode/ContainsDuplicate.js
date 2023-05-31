// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let arr = [];
    for (let num of nums) {
        if (arr.includes(num)) {
            return true
        } else {
            arr.push(num)
        }
    }
    return false
};
