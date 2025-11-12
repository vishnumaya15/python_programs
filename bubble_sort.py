nums = [5, 2, 9, 1, 7]

for i in range(len(nums)):
    print(i,"i")
    for j in range(len(nums) - i - 1):
        print(j,"j")
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)  #[1, 2, 5, 7, 9]