class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        n=len(nums)
        for i in range (n):
            if nums[i]!=0:
             
                nums[i] ,nums[k]=nums[k], nums[i]
                k=k+1
                
                
        return  nums      