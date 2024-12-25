from utils.get_data import *
from typing import Tuple, List
import argparse

# [a,b] num a -> block-size | num b -> free space. Each 2, new ID

def build_space(data, part) -> Tuple[List[str], str]:
    cnt = 2
    file_system = []
    total_free_space = 0
    last_ID = 0

    while cnt < len(data):
        ID = str((cnt//2) - 1);
        block_size = int(data[cnt-2])
        free_space = int(data[cnt-1])
        
        for _ in range(block_size): file_system.append(ID)
        for _ in range(free_space): 
            file_system.append('.')
            total_free_space += 1

        last_ID = ID
        cnt += 2
    
    if len(data) % 2 != 0:
        ID = str(int(last_ID) + 1)
        block_size = int(data[len(data) - 1])
        for _ in range(block_size): file_system.append(ID)
    
    part_return = ''

    if part == 1:
        part_return = total_free_space
    else:
        part_return = last_ID

    return file_system, part_return

def swap(item, idx, cnt, list) -> None:
    aux = list[idx]
    list[idx] = item
    list[cnt] = aux

def rearange_blocks(file_system, free_space) -> List[str]:
    #Coger ultimo numero, swapearlo con la primera aparición de un '.', Solo si es un numero
    #Recorrer desde atrás
    cnt = len(file_system) - 1
    idx = file_system.index('.')

    end = len(file_system) - free_space

    while idx != end:
        item = file_system[cnt]
        if item != '.':
            swap(item, idx, cnt, file_system)
        cnt -= 1
        idx = file_system.index('.')
        # print(file_system)
    
    return file_system

def block_swap(sl1, sl2, fs) -> None:
    b1 = fs[sl1[0]:sl1[1]+1]
    b2 = fs[sl2[0]:sl2[1]+1]

    
    fs[sl1[0]:sl1[1]+1] = b2
    fs[sl2[0]:sl2[1]+1] = b1

# Devuelve posición inicial donde cabe el bloque
def find_space(fs, cant, max) -> int:
    space = 0
    for i, char in enumerate(fs):
        if i == max: break
        if char == '.':
            space += 1
        else:
            space = 0
            continue
        
        if space == cant:
            return i - (cant - 1)
    
    return 0

def rearange_blocks_v2(file_system, last_id) -> List[str]:

    for i in range(int(last_id)+1, 0, -1):
        cant = file_system.count(str(i))
        act_pos = file_system.index(str(i))

        pos_ini = find_space(file_system, cant, act_pos)
        if pos_ini != 0:
            block_swap((pos_ini, pos_ini + (cant - 1)), (act_pos, act_pos+ (cant - 1)), file_system)
    
    return file_system


def calc_checksum(file_system) -> int:
    total = 0
    for i, num in enumerate(file_system):
        if num == '.': continue
        total += i * int(num)
    return total

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description= "AOC Day 9")
    parser.add_argument('--part', type=int, choices=[1,2], default=1, help="Choose Day 9 Part")

    args = parser.parse_args()

    data = get_data(9)
    # data = read_from_file()
    data = data.replace('\n', '')
    file_system, free_space = build_space(data, args.part)

    if args.part == 1:
        # Part1
        file_system = rearange_blocks(file_system, free_space)
    else:
        # Part 2
        file_system = rearange_blocks_v2(file_system, free_space)
    
    total = calc_checksum(file_system)
    print(total)