class Solution(object):
    def isPalindrome(self, x):
        return x >= 0 and x == int(str(x)[::-1])


f = 121
s = 123
t = -121

print(f'{f}: {Solution().isPalindrome(f)}')
print(f"{s}: {Solution().isPalindrome(s)}")
print(f"{t}: {Solution().isPalindrome(t)}")