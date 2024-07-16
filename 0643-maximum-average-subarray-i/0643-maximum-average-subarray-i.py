class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        max_sum=0
        
        #Fixes the window
        for i in range(k):
            sum += nums[i]
        max_sum = sum
        
        #increments one by one until the end storing the max_sum of the window
        for i in range(k, len(nums)):
            sum += nums[i]
            sum -= nums[i-k]

            max_sum = max(max_sum,sum)

        avg = max_sum/k
        return avg    
#Time Complexity: O(n) 
#Space Complexity: O(1)
        
        
#Time Complexity Too high --->

        
        # for i in range(len(nums)):
        #     # print("i=",i)
        #     if len(nums)>1:
        #         if i <= len(nums)-k:
        #             for j in range(k):
        #                 # print("j=",j)
        #                 t = i+j
        #                 if  t <= len(nums)-1:
        #                     # print("i+j=",t)
        #                     # print("num[i+j]=", nums[i+j])
        #                     sum = sum + nums[t]
        #                     # print("sum:",sum)
        #             if sum > max_sum:
        #                 max_sum = sum
        #                 # print("max sum=",max_sum)
        #             sum=0
        #     else:
        #         max_sum = nums[0]
        # ans = max_sum/k
        # return ans