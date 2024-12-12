import time
import os

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 4"), 'r')
matrix = []
counter = 0
for l in file:
    counter += l.count("XMAS")
    counter += l.count("SAMX")
    matrix.append(list(l.replace('\n', '')))

#search vertically
for i in range(0, len(matrix[0])):
    counter += "".join([matrix[j][i]for j in range(0, len(matrix))]).count("XMAS")
    counter += "".join([matrix[j][i] for j in range(0, len(matrix))]).count("SAMX")

#Search Diagonally in all 4 directions
cols=len(matrix[0])
rows=len(matrix)
for i in range(0, len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "X":
            if (i+3)<rows and (j+3)<cols:
                current = ''
                for k in range(0, 4):
                    current += matrix[i+k][j+k]
                counter += current.count("XMAS")
                counter += current.count("SAMX")
            if (i-3)>=0 and (j-3)>=0:
                current = ''
                for k in range(0, 4):
                    current += matrix[i-k][j-k]
                counter += current.count("XMAS")
                counter += current.count("SAMX")
            if (i-3)>=0 and (j+3)<cols:
                current = ''
                for k in range(0, 4):
                    current += matrix[i - k][j + k]
                counter += current.count("XMAS")
                counter += current.count("SAMX")
            if (i+3)<rows and (j-3)>=0:
                current = ''
                for k in range(0, 4):
                    current += matrix[i + k][j - k]
                counter += current.count("XMAS")
                counter += current.count("SAMX")

end_p1 = time.time()
print("Part 1 result: {}".format(counter))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()

start_p2 = time.time()

counter = 0
cols=len(matrix[0])
rows=len(matrix)
for i in range(0, len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "A" and (i!=0) and (j!=0) and (i<rows-1) and (j<cols-1):
            x1 = "".join([matrix[i-1][j-1], matrix[i][j], matrix[i+1][j+1]])
            x2 = "".join([matrix[i+1][j-1], matrix[i][j], matrix[i-1][j+1]])
            if (x1 == "MAS" or x1 == "SAM") and (x2 == "MAS" or x2 == "SAM"):
                counter += 1


end_p2 = time.time()
print("Part 2 result: {}".format(counter))
print("The time of execution of above program is :", (end_p2 - start_p2) * 10**3, "ms")
print()