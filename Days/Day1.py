import requests
from utils.config import COOKIES, URL

day = 1
url = URL.format(day)

data = requests.get(url, headers={'Cookie': COOKIES})


data = data.text

test = data.split("\n") # [n1 n2,n3 n4]

# with open("output.txt", "r") as file:
#     test = file.read()

# test = test.split("\n")


list_0 = []
list_1 = []

map_sol = {}

for pair in test:
    if(pair == ""): break

    aux = pair.replace("  ", "").split(" ")
    list_0.append(int(aux[0]))
    # list_1.append(int(aux[1]))
    
    #Part 2
    val = int(aux[1])

    if val in map_sol:
        map_sol[val] = map_sol[val] + 1
    else:
        map_sol[val] = 1
    
    

# list_0.sort()
# list_1.sort()

# total = 0
# for i in range(len(list_1)):
#     total += abs(list_0[i] - list_1[i])

# print(total)
total = 0

for num in list_0:
    if num in map_sol:
        total += num * map_sol[num]

print(total)

