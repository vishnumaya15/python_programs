def find_missing(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)
list=[1,2,3,5]
print(find_missing(list))