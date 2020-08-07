import os
import requests


#cycle

#check if number is in all ranges
#if it is in all ranges, bill all usage on that tiers 
#if its not in all ranges then count the amount of numbers it is in
#constants: counter(Counting each range) number

num = 21
counter = 0
charge = 0.00

list_ranges = [[0, 16, 6.03], [16,25, 7.59], [25,28, 9.40], [28,35, 9.40]]
selected_tier = list_ranges[3] 

for test in list_ranges:
    for check in range(test[0], test[1]):
        if check <= num: 
            print(check)
            counter = counter + 1
            charge += test[3] 
        else: 
            print("Not greater than 8")

"""
for check in range(0, 16): 
    if check <= num: 
        print(check)
        counter = counter + 1
        charge += 6.03
    else: 
        print("Not greater than 8")

print(charge) 
"""
