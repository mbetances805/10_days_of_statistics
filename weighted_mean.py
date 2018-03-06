def calculate_weighted_mean(list_length, input_list, list_weight):
    if len(input_list) != len(list_weight):
        return 'Unable to calculate weighted average'
    
    sum_of_products = 0
    sum_of_weights = 0
    for x in range(0, len(input_list)):
        sum_of_products += (input_list[x] * list_weight[x])
        sum_of_weights += list_weight[x]

    weighted_average = round(sum_of_products / sum_of_weights, 1)
    
    print(weighted_average)
    return weighted_average
    
# Or solved with numpy
# import numpy as np
# 
# def calculate_weighted_mean(length, num_list, num_weight):
# 
#     weighted_average = round(np.average(num_list, weights=num_weight), 1)
# 
#     print(weighted_average)
#     return weighted_average

list_length = int(input())
input_list = [int(num) for num in input().split(' ')]
list_weight = [int(num) for num in input().split(' ')]
calculate_weighted_mean(list_length, input_list, list_weight)