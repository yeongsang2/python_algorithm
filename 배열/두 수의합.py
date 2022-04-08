def twoSum(nums:list[int], target:int)-> list[int]:

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def twoSum2(nums:list[int], target):
    for i,v  in enumerate(nums):
        complement = target - v

        if complement in nums[i+1:]:
            return [nums.index(v), nums[i+1:].index(complement) + (i+1)]
        
def twoSum3(nums:list[int], target):
    nums_map = {}
    for i,num in enumerate(nums):
        nums_map[num] = i

    for i, num  in enumerate(nums):
        complement = target- num
        if complement in nums_map and i != nums_map:
            return [nums.index(num), nums_map[complement]]    


print(twoSum3([2,7,11,15], 9))


