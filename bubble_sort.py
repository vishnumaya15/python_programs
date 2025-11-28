nums = [5, 2, 9, 1, 7]

for i in range(len(nums)):

    for j in range(len(nums) - i - 1):

        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)  #[1, 2, 5, 7, 9]

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print (nums)

