class Solution(object):
    def isPalindrome(self, x):
        number = []
        for _ in str(abs(x)):
            number.append(int(_))
        reversed_numbers = list(reversed(number))
        joined_number = int(''.join(map(str, reversed_numbers)))
        if x<0:
            answer = False
        else:
            if x == joined_number:
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