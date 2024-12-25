from utils.get_data import get_data

data = get_data(5)

# with open("input.txt", "r") as file:
#     data = file.read()

#Lista de cosas que ordenar -> vector ordenado con estas normas
#busqueda binaria por cada update.

#Get all numbers ordered correctly according to rules
data = data.split("\n")

rules = []
updates = []

def fix_array(update, order):
    print(update, "Hay que solucionar")
    nums = []
    for page in update:
        if len(nums) == 0:
            nums.append(page)
            continue
        
        if page in order.keys(): 
            antes_de = order[page]
            #los numeros de antes_de si estan ya en el nums
            min_idx = 100
            for i in antes_de:
                if i in nums:
                    #no válido, modificar
                    idx = nums.index(i)
                    min_idx = min(idx, min_idx)
            nums.insert(min_idx, page)

    print(nums, "solucionado!")
    return int(nums[len(nums)//2])



for item in data:

    if item == '': continue
    if '|' in item: rules.append(item)
    else: updates.append(item)

order = {}

for num in rules:
    # X | Y -> X tiene que ir antes que Y
    aux = num.split('|')
    x = aux[0]
    y = aux[1]

    if x not in order.keys():
        order[x] = []
    order[x].append(y)

print(order)
result = 0
for u in updates:
    aux = u.split(',')
    #evaluamos la update u esta correcta
    nums = [] #set
    for page in aux:
        if len(nums) == 0:
            nums.append(page)
            continue
        
        if page in order.keys(): 
            antes_de = order[page]
            #los numeros de antes_de si estan ya en el nums
            error = False
            for i in antes_de:
                if i in nums:
                    #no válido
                    error = True
                    break
            
            if error: break
            
        nums.append(page)
    
    if len(nums) == len(aux):
        # result += int(aux[len(aux)//2])
        continue
    else:
        result += fix_array(aux, order)
    

print(result)
        


