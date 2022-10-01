"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numberList):
    if(len(numbers) % 2 == 0):
        #print(len(numbers))
        index1 = int(len(numbers)/2)
        index2 = int(index1-1)
        median = numbers[index1] + numbers[index2]
        median = median/2
    else:
        index1 = int(len(numbers) -1)
        median = numbers[index1]
    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(median(numbers))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
