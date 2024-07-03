class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
        if count >= 1:
            for j in range(count):
                for i in range(len(nums)-1):
                    if nums[i] == 0:
                        temp = nums[i]
                        nums[i] = nums[i+1]
                        nums[i+1] = temp

