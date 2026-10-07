class Solution:
    def findMin(self, nums: list[int]) -> int:
        mini=float("inf")
        n=len(nums)
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]<=nums[j]:
                mini=min(mini,nums[mid])
                j=mid-1
            else:
                mini=min(mini,nums[i])
                i=mid+1
        return mini

