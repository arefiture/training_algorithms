class Solution:
    def isPalindromeMath(self, x: int) -> bool:
        start_number = x
        reverse_number = 0
        while start_number > 0:
            diff = start_number % 10
            reverse_number = reverse_number * 10 + diff
            start_number = (start_number - diff) // 10
        return x == reverse_number

    def isPalindrome(self, x: int) -> bool:
        return (number := str(x)) == number[::-1]


solution = Solution()

print('Example 1:', solution.isPalindrome(x=121))
print('Example 2:', solution.isPalindrome(x=-121))
print('Example 3:', solution.isPalindrome(x=10))
