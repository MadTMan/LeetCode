class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        output = []

        for num in range(length-1):
            for i in range(num+1,length):
                if nums[num] + nums[i] == target:
                    return [num,i]