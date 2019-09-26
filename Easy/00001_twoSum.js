
// https://leetcode.com/problems/two-sum/description/

// 1. Two Sum

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:
// Given nums = [2, 7, 11, 15], target = 9,
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

//////////////////////////////////////////////////
var twoSum = function(nums, target) {
	let n = nums.length;
	for ( let i = 0; i < n - 1; i++) {
		for ( let j = i + 1; j < n; j++) {
			if (nums[i] + nums[j] === target) {
				return [i, j]
			}
		}
	}
};

//////////////////////////////////////////////////
var twoSum = function(nums, target) {
	let map = {};
	for (let i = 0; i < nums.length; i++) {
		let tmp = map[target - nums[i]]
		if (tmp !== undefined) {
			return [tmp, i]
		}
		map[nums[i]] = i
	}
}
