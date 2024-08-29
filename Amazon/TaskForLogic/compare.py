import main
import answer

matrix = [2, 3, 5, 7, -9,
          4, 11, -8, -10, 12,
          -17, 3, -24, -2, -5,
          7, -10, -12, 8, 16,
          -14, 3, -2, 1, 9]

line = "__________________________________________________________|"

print(f"\n{line}")
print(f"main.py: {main.max_matrix_sum(matrix)}")
print(f"answer.py: {answer.max_matrix_sum(matrix)}")
print(line)
print(f"Execution time (main.py): {main.execution_time:.20f} seconds")
print(f"Execution time (answer.py): {answer.execution_time:.20f} seconds")
print(line)
