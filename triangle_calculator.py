file1 = open("triangle.txt", "r")
triangle = file1.readlines()


#Global variables
triList = []

for line in triangle:
    StringList = line.split()
    IntList = list(map(int, StringList))
    triList.append(IntList)

# Using dynamic programming I want to go through the list starting from the bottom row and work my way up,
# while adding the new number to the row above so that I in the end finally have one final number at the top of the list/triangle.

rowIndex = len(triList) - 2
while rowIndex >= 0:
    colIndex = 0
    while colIndex <= rowIndex:
        currentNumber = triList[rowIndex][colIndex]
        leftAdjacent = triList[rowIndex+1][colIndex]
        rightAdjacent = triList[rowIndex+1][colIndex+1]
        currentNumber = max(currentNumber+leftAdjacent,currentNumber+rightAdjacent)
        triList[rowIndex][colIndex] = currentNumber
        colIndex += 1
    rowIndex -= 1

print("Result: " + str(triList[0][0]))