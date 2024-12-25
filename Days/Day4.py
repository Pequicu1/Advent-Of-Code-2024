from utils.get_data import get_data

data = get_data(4)

# with open("input.txt", "r") as file:
#     data = file.read()

aux = data.split("\n")

matrix = [[0 for _ in range(len(aux)-1)] for _ in range(len(aux)-1)]

def check_xmas(row):
    aux = ""
    it = 0
    total = 0
    for letter in row:
        aux += letter
        if aux[len(aux)-1] == XMAS[it]:
            it += 1
        else:
            if aux[len(aux)-1] == 'X':
                aux = 'X'
                it = 1
                continue
            else:
                it = 0
                aux = ""
                continue
        
        if it == 4:
            total += 1
            it = 0
            aux = ''
    
    return total

def get_diagonals(matrix):
    diagonals = []

    # Get all diagonals from top-left to bottom-right
    for p in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for q in range(max(p - len(matrix[0]) + 1, 0), min(p + 1, len(matrix))):
            diagonal.append(matrix[q][p - q])
        diagonals.append(diagonal)

    # Get all diagonals from top-right to bottom-left
    for p in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for q in range(max(p - len(matrix[0]) + 1, 0), min(p + 1, len(matrix))):
            diagonal.append(matrix[q][len(matrix[0]) - 1 - (p - q)])
        diagonals.append(diagonal)

    return diagonals

# Datos a matriz
i = 0
for row in aux:
    j = 0
    for item in row:
        matrix[i][j] = item
        j += 1
    i += 1

print(matrix)

ROWS = len(matrix)
COLS = len(matrix[0])

XMAS = "XMAS"

result = 0

#Check rows forward and backwards
for row in matrix:
    result += check_xmas(row)
    result += check_xmas(row[::-1])

transposed_matrix = list(map(list, zip(*matrix)))


#Check cols forward and backwards
for col in transposed_matrix:
    result += check_xmas(col)
    result += check_xmas(col[::-1])

#Check diag forward and backwards

diagonals = get_diagonals(matrix)

diagonals = [diag for diag in diagonals if len(diag) >= 4]


for diag in diagonals:
    result += check_xmas(diag)
    result += check_xmas(diag[::-1])

print(result)


