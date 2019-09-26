# https://leetcode.com/problems/two-sum/description/

# 1. Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#######################################################
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	print
	val_index = {}
	for i in xrange(len(nums)): 
		tmp = target - nums[i]
		if tmp in val_index:
			return [val_index[tmp] + 1, i + 1]
		val_index[nums[i]] = i


#######################################################
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	n = len(nums)
	pairs = sorted(zip(nums, range(n)))
	start, end = 0, n - 1
	while start < end:
		num1, idx1 = pairs[start]
		num2, idx2 = pairs[end]
		need = target - num1
		if num2 > need:
			end -= 1
		elif num2 < need:
			start += 1
		else:
			return [pairs[start][1], pairs[end][1]]


assert twoSum([2,7,11,15], 9) == [0, 1]
assert twoSum([5, 3, 9, 1, 10], 12) == [1, 2]
