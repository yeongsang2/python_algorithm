class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = [ ] # 반환
        nums.sort()
        
        for i in range(len(nums)- 2):
            
            # 중복된 값 건너뛰기 -> 이전 값이랑 동일하다면 스킵해야지
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1 , len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                    
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0 이므로 정답처리
                    results.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    
                    left +=1
                    right -=1
            
        return results


solution1 = Solution()
nums = [-1,0,1,2,-1,-4]
a= solution1.threeSum(nums)
print(a)