from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''

        min_length = min(len(s) for s in strs)
        first_word = strs[0]

        i = 0
        while i < min_length:
            char = first_word[i]

            if all(char == s[i] for s in strs):
                i += 1
            else:
                break

        return first_word[:i]


solution = Solution()

print('Example 1:', solution.longestCommonPrefix(
    strs=['flower', 'flow', 'flight'])
)
print('Example 2:', solution.longestCommonPrefix(
    strs=['dog', 'racecar', 'car'])
)
