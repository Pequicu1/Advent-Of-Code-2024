from utils.get_data import get_data
import re

data = get_data(3)

with open("input.txt", "r") as file:
    data = file.read()

regexp = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
matches = re.findall(regexp, data)

mult = True
result = 0
for i in matches:

    # do has appeared before, we mult
    if mult and i[0] != '':
        aux = i[0].replace("mul(", "").replace(")", "").split(',')
        result += int(aux[0]) * int(aux[1])
    #do
    elif i[1] != '' and not mult:
        mult = True
    #don't
    elif i[2] != '' and mult:
        mult = False


print(result)