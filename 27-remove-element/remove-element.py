class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)
        for k in range(0,n):
            if nums[k]!=val:
                nums[i]=nums[k]
                i=i+1
        return i