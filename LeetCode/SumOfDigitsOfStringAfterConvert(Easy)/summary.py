from solution1 import Solution as solution1
from solution2 import Solution as solution2
from solution3 import Solution as solution3
import time

start = time.time()
print(f"Solution1: {solution1.getLucky(self=None, s='hello', k=1)}")
end = time.time()
elapsed = end - start
print(f"Solution1 speed: {elapsed:.20f} seconds")

start = time.time()
print(f"Solution2: {solution2.getLucky(self=None, s='hello', k=1)}")
end = time.time()
elapsed = end - start
print(f"Solution2 speed: {elapsed:.20f} seconds")

start = time.time()
print(f"Solution3: {solution3.getLucky(self=None, s='hello', k=1)}")
end = time.time()
elapsed = end - start
print(f"Solution3 speed: {elapsed:.20f} seconds")
