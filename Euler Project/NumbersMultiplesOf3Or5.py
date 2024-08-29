class Solution:
    def numbers_multiples_three_or_five(n: int) -> int:
        list = []
        for i in range(n):
            if (i / 3).is_integer() or (i / 5).is_integer():
                list.append(i)
        return sum(list)


print(Solution.numbers_multiples_three_or_five(10))
