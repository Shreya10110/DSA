class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        sum=0
        while(temp>0):
            digit=temp%10
            sum=sum*10+digit
            temp=temp//10
        if sum==x:
            return True
        else:
            return False
        