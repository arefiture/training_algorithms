class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        if number != number[::-1]:
            return False
        return True


solution = Solution()

print('Example 1:', solution.isPalindrome(x=121))
print('Example 2:', solution.isPalindrome(x=-121))
print('Example 3:', solution.isPalindrome(x=10))
