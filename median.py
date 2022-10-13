"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        median = 0
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if(len(numbers) % 2 == 1):
            median = (numbers[int((len(numbers) - 1 )/ 2)])
        else:
            middle1 = numbers[int((len(numbers)/2) - 1)]
            middle2 = numbers[int(len(numbers)/2)]
            median = (middle1 + middle2) / 2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)