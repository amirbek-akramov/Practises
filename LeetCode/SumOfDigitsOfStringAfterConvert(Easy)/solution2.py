class Solution:
    def getLucky(self, s, k):
        s = s.lower()
        s = s.replace(" ", "")

        s = ''.join(str(ord(c) - ord('a') + 1) for c in s)

        for _ in range(k):
            s = str(sum(int(digit) for digit in s))

        return int(s)
