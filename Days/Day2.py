from utils.get_data import get_data

data = get_data(2)


# with open("input.txt", "r") as file:
#     data = file.read()

data = data.split("\n")

result = 0

for row in data:
    
    if row == '': 
        continue
    
    level = row.split(" ")

    asc = None
    safe = True

    if int(level[0]) > int(level[1]):
        asc = False
    elif int(level[0]) < int(level[1]):
        asc = True

    print(level)

    error_count = 0

    for i in range(1, len(level)):

        if error_count > 1: break

        prev = int(level[i-1])
        act = int(level[i])

        if abs(prev - act) > 3 or abs(prev - act) == 0:
            error_count += 1
            continue

        if prev < act and not asc:
            error_count += 1
            continue

        elif prev > act and asc:
            error_count += 1
            continue
    
    if safe and error_count <= 1:
        result += 1

print(result)
