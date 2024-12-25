from utils.get_data import get_data

data = get_data(4)

# with open("input.txt", "r") as file:
#     data = file.read()

aux = data.split("\n")

matrix = [[0 for _ in range(len(aux)-1)] for _ in range(len(aux)-1)]

i = 0
for row in aux:
    j = 0
    for item in row:
        matrix[i][j] = item
        j += 1
    i += 1

ROWS = len(matrix)
COLS = len(matrix[0])

MAS = "MAS"

result = 0

for i in range(1, ROWS-1):
    for j in range(1, COLS-1):
        if matrix[i][j] == 'A':
            w1 = matrix[i-1][j-1] + 'A' + matrix[i+1][j+1]
            w2 = matrix[i+1][j-1] + 'A' + matrix[i-1][j+1]


            if (w1 == MAS or w1 == MAS[::-1]) and (w2 == MAS or w2 == MAS[::-1]):
                print(w1, w2)
                result += 1

print(result)