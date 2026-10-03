class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return True
            if nums[i]==nums[mid]==nums[j]:
                i=i+1
                j=j-1
                continue
            if nums[mid]<=nums[j]:
                if nums[mid]<=target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
            else:
                if nums[i]<=target<=nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
        return False


            
