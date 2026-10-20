nums = [1, 2, 3, 4, 5, 6]
oddsum =0
evensum=0
for num in nums:
    if num%2 ==0:
         evensum +=num
    else:
        oddsum+=num
print(f"Oddsum:{oddsum}")
print(f"Evensum:{evensum}")
        