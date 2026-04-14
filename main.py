def two_sum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                result.append(nums[i])
                result.append(nums[j])
                return result

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
#Answer: [2, 7]