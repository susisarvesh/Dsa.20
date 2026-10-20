nums = [10, 20, 30, 40, 50]

def reverse(nums):
    for i in range(len(nums)//2):
        temp = nums[i]
        nums[i] = nums[len(nums)-1-i]
        nums[len(nums)-1-i] = temp
        


    return nums


print(len(nums)//2)
print(reverse(nums))