class Solution:
    def getLucky(self, s, k):
        s = s.lower()
        s = s.replace(" ", "")
        s = [ord(c) - ord('a') + 1 for c in s]

        s = sum(int(digit) for num in s for digit in str(num))

        for _ in range(k - 1):
            s = sum(int(digit) for digit in str(s))

        return s
