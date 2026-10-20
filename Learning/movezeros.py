#move zeros to end
# 3. Move All Zeros to the End
# Easy

# Given an integer array nums, move all zeros to the end while maintaining the relative order of nonzero elements.

# Example

# Input: nums = [0, 1, 0, 3, 12]

# Output: [1, 3, 12, 0, 0] 

# Constraint: Modify the array in-place.
nums = [0, 1, 0, 3, 12]
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
            temp  = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j+=1
print(nums)



 
