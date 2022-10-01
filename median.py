"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numberList):
    for i in range(len(numberList)):
        lowest = numberList[i]
        for j in range(0,len(numberList)):
            #print(i,j)
            if numberList[j] > numberList[i]:
                c = numberList[i]
                numberList[i] = numberList[j]
                numberList[j] = c
    #print(numberList)
    index1 = 0
    length = len(numberList)
    #print("len" , length)
    if(length % 2 == 0):
        #print(len(numbers))
        index0 = length/2
        index1 = int(index0)
        index2 = index1-1
        #print(index1)
        median = numberList[index1] + numberList[index2]
        median = median/2
    else:
        index0 = length/2
        #print(index0)
        index1 = int(index0)
        #print(index1)
        median = numberList[index1]
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
#print(numbers)
