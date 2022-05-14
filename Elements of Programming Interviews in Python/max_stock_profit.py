from configparser import MAX_INTERPOLATION_DEPTH
import math

def calculate_max(S):
    min_element = math.inf
    max_profit = 0
    for element in S:
        if element < min_element:
            min_element = element
        if element - min_element > max_profit:
            max_profit = element - min_element
    return max_profit

print(calculate_max([3,10,2,20,30,0,10]))