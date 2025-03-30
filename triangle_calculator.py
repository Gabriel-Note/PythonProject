
# opening and reading the textfiles
# Using 3 different ones for testing purposes
file1 = open("triangle.txt", "r")
file2 = open("triangle0.txt", "r")
file3 = open("triangle1.txt", "r")

triangle = file1.readlines()
triangle0 = file2.readlines()
triangle1 = file3.readlines()



# smallList = [
#         3,
#        7,4,
#       2,4,6,
#      8,5,9,3,
#     5,6,2,9,4
# ]
# smallList2 = [
#     [3],
#     [7,4],
#     [2,4,6],
#     [8,5,9,3],
#     [5,6,2,9,4]
# ]

triList = []

# Creating a nested list and converting to Int using
for line in triangle0:
    StringList = line.split()
    IntList = list(map(int, StringList))
    triList.append(IntList)

# for line in triangle:
#     StringList = line.split()
#     IntList = list(map(int, StringList))
#     triList.append(IntList)


print("new line")
print(triList)
print(triList[2][2])
print(triList[2][2] + triList[3][3])






#print(triangle0)
#print(smallList2[1][1])