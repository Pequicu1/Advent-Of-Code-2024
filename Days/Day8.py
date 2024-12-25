from utils.get_data import *


#Para cada antena, mirar todas las otras antenas con el mismo identificador. Encontrar la distancia que las separa, y poner un '#'
# en la siguiente posición que le correspondería.

# 1 -> Input: hacer mapa 'antena' : [posicion]
# 2 -> Recorrer mapa por antenas, encontrar distancia, poner # eliminar posicion.

def get_antennas(data):
    rows = data.split('\n')
    inp_map = []
    antennas = {}
    for i, row in enumerate(rows):
        if row == '': continue
        
        for j, c in enumerate(row):
            if c != '.':
                #crear entrada mapa o añadir posición
                if c not in antennas.keys():
                    antennas[c] = [(i,j)]
                else: antennas[c].append((i,j))
        #añadir al mapa (matriz)
        inp_map.append(row)

    return inp_map, antennas

def add_tuples(t1,t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def sub_tuples(t1,t2):
    return (t1[0] - t2[0], t1[1] - t2[1])

def out_of_bound(pos, i_max, y_max):
    return (pos[0] >= i_max or pos[0] < 0 or pos[1] >= y_max or pos[1] < 0)

def calculate_positions(u1, u2, i_max, y_max):
    #encontrar distancia entre dos puntos.
    antinode_positions = []
    dist = (u1[0] - u2[0], u1[1] - u2[1])
    #Desde u1 hasta fin
    while not out_of_bound(u1, i_max, y_max):
        u1 = add_tuples(u1,dist)
        antinode_positions.append(u1)

    #Desde u2 hasta fin
    while not out_of_bound(u2, i_max, y_max):
        u2 = sub_tuples(u2,dist)
        antinode_positions.append(u2)

    return antinode_positions

#Ubis -> todas las posiciones en las que se encuentra una antena de un cierto tipo.
def calculate_antinode_positions(ubis, i_max, y_max):
    positions = []

    while len(ubis) != 0:
        ubi = ubis[0]
        ubis.pop(0)
        for u in ubis:
            positions += calculate_positions(ubi, u, i_max, y_max)
    
    return positions

def set_antinode_in_map(pos, mapa) -> None:
    row = mapa[pos[0]]
    new_row = row[:pos[1]] + '#' + row[pos[1] + 1:]
    mapa[pos[0]] = new_row
    return


def find_antinodes(antennas, antennas_map) -> int:
    antinodes = 0
    for antenna in antennas:
        ubis = antennas[antenna]
        if len(ubis) > 1: antinodes += len(ubis)
        positions = calculate_antinode_positions(ubis, len(antennas_map), len(antennas_map[0]))
        for pos in positions:
            if pos[0] >= len(antennas_map) or pos[0] < 0 or pos[1] >= len(antennas_map[0]) or pos[1] < 0: 
                continue

            if antennas_map[pos[0]][pos[1]] == ".":
                set_antinode_in_map(pos, antennas_map)
                antinodes += 1

    return antinodes

if __name__ == '__main__':    
    data = get_data(8)
    # data = read_from_file()
    antennas_map, antennas = get_antennas(data)
    antinodes = find_antinodes(antennas, antennas_map)
    print(antinodes)

    # print(antenna_map)
    # print(antennas)