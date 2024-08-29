import time

start_time = time.time()
def max_matrix_sum(matrix):
    total_sum = 0
    negative_count = 0
    min_abs_value = float('inf')

    for num in matrix:
        total_sum += abs(num)
        if num < 0:
            negative_count += 1
        min_abs_value = min(min_abs_value, abs(num))

    # If the count of negative numbers is even, return the total sum.
    # Otherwise, subtract twice the minimum absolute value from the total sum.
    if negative_count % 2 == 0:
        return total_sum
    else:
        return total_sum - 2 * min_abs_value

end_time = time.time()
execution_time = end_time - start_time