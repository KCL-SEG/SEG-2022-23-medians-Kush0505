"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numberList):
    if(numbers.size() % 2 == 0):
        index1 = numbers.size()/2
        index2 = index1 +1
        median = numbers[index1] + numbers[index2]
        median = median/2
    else:
        index1 = numbers.size() +1
        median = numbers[index1]
    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
