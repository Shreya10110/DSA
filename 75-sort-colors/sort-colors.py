class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        for i in range(n):
            min_ind=i
            for j in range(i+1,n):
                if nums[min_ind]>nums[j]:
                    nums[min_ind],nums[j]=nums[j],nums[min_ind]
        return(nums)
        