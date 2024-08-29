# class Solution:
#     def temperature(n: int, nums: list) -> list:
#         dicty = {}
#         x = 0
#         i = 1
#         if x < n:
#             for num in nums:
#                 if num > nums[i]:
#                     dicty[num] = i
#                     i += 1
#                     x += 1
#         return dicty
#
#

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_

# class Solution:
#     def temperature(nums: list):
#         answer = {}
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i <= (len(nums)):
#                     j = i + 1
#                     if nums[j] > nums[i]:
#                         answer[j] = i
#                         break
#         return answer

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_



sol = Solution.temperature([13, 12, 15, 11, 9, 12, 16])
print(sol)
