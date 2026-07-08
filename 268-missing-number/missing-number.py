class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums=0
        for i in nums:
            sum_nums=sum_nums+i
            ans=0
        for j in range(0,len(nums)+1):
            ans=ans+j
        total=ans-sum_nums    
        return total