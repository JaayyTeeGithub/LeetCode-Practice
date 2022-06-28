class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for index in range(0,len(nums)):
            
            if index == 0:
                right = sum(nums[1:len(nums)])
                left = 0
                
                if right == left:
                    return index

            elif index == len(nums):
                left = sum(nums[0:len(nums) - 1])
                right = 0
                
                if right == left:
                    return index

            else:
                right = sum(nums[(index + 1): len(nums)])
                left = sum(nums[0:index])
                
                if right == left:
                    return index
       
            
        return -1