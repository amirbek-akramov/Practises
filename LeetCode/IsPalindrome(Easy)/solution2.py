class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            answer = False
        else:
            if x == int(str(x)[::-1]):
                answer = True
            else:
                answer = False
        return answer


f = 121
s = 123
t = -121

print(f'{f}: {Solution().isPalindrome(f)}')
print(f"{s}: {Solution().isPalindrome(s)}")
print(f"{t}: {Solution().isPalindrome(t)}")