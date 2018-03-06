import math

def calculate_standard_deviation(list_length, num_list):
    total_sum = sum(num_list)
    list_mean = total_sum / list_length
    squared_distance_list = 0
    
    for num in num_list:
        squared_distance_list += ((num - list_mean)**2)
    
    standard_deviation = round(math.sqrt(squared_distance_list / list_length), 1)
    
    print(standard_deviation)
    return standard_deviation
    

input_size = int(input())
input_list = [int(num) for num in input().split(' ')]
calculate_standard_deviation(input_size, input_list)