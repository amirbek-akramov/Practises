from solution1 import Solution as solution1
import time

print("|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|")
print('Solution 1')
print("____________________________________________________________|")
start_time = time.time()
print("Roman to Integer 1994: ", solution1().romanToInt(s="MCMXCIV"))
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time: {execution_time:.6f} ms")

start_time = time.time()
print("Roman to Integer 2024: ", solution1().romanToInt(s="MMXXIV"))
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time: {execution_time:.6f} ms")

start_time = time.time()
print("Romam to Integer 3900: ", solution1().romanToInt(s="MMMCMXC"))
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time: {execution_time:.6f} ms")

start_time = time.time()
print("Roman to Integer 3999: ", solution1.romanToInt(s="MMMCMXCIX"))
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time: {execution_time:.6f} ms")
