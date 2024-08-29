import time

start_time = time.time()
def max_matrix_sum(matrix):
    positive = []
    negative = []
    for i in matrix:
        if i<0:
            negative.append(i)
        else:
            positive.append(i)
    negative_sum = abs(sum(negative))
    min_pos = sorted(positive).pop(0)
    if len(negative)%2==0:
        answer = negative_sum + sum(positive)
    else:
        answer = negative_sum + sum(positive) - min_pos*2

    return answer

end_time = time.time()
execution_time = end_time - start_time