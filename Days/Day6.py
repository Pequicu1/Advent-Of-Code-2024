from utils.get_data import get_data, read_from_file
import os
import time

UP = (-1,0)

# data = get_data(6)
data = read_from_file()

data = data.split("\n")


matrix = [['' for _ in range(len(data)-1)] for _ in range(len(data)-1)]

i = 0
guard_ini_pos = (0,0)
for row in data:
    if row == '': continue
    j = 0
    for item in row:
        if item == '^': guard_ini_pos = (i,j)
        matrix[i][j] = item
        j += 1
    i += 1

def guard_out_of_map(i,j,max):
    return (i > max-1 or i < 0) or (j > max-1 or j < 0)

def get_new_pos(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def imprimir_matriz(matrix, pos, dir):
    os.system('cls')  # Limpiar la pantalla en Windows
    for fila in matrix:
        print(' '.join(fila))
    print("Pos: ", pos, "Dir: ", dir)
    time.sleep(0.05)  # Pausa para ver el frame


def try_for_obstruction(matrix_ini, pos, dir):
    return bool 

TOTAL = 0

def calculate_path(guard_act_pos, guard_prev_pos, guard_act_dir, searching, goal_pos, matrix):
    global TOTAL
    while not guard_out_of_map(guard_act_pos[0], guard_act_pos[1], len(matrix)):
        
        if guard_act_pos == goal_pos:
            #Hemos llegado a un bucle
            return True

        item_act = matrix[guard_act_pos[0]][guard_act_pos[1]]


        if item_act == '#':
            #Rotamos a la derecha
            guard_act_pos_or = guard_prev_pos
            guard_act_dir_or = (guard_act_dir[1], -guard_act_dir[0])
            #Empezar a calcular posible bloqueo
            #Añadir bloqueo delante del giro
            if not searching:
                obj_pos = get_new_pos(guard_act_pos_or, guard_act_dir_or)
                matrix[obj_pos[0]][obj_pos[1]] = '#'
                
                guard_act_pos = guard_prev_pos
                guard_act_dir = (guard_act_dir_or[1], -guard_act_dir_or[0])
                guard_prev_pos = guard_act_pos
                guard_act_pos = get_new_pos(guard_act_pos, guard_act_dir)

                TOTAL += calculate_path(guard_act_pos, guard_prev_pos, guard_act_dir, True, guard_prev_pos, matrix)
                print("Total:", TOTAL)
                searching = False
                matrix[obj_pos[0]][obj_pos[1]] = '.'
                guard_act_dir = guard_act_dir_or
                guard_act_pos = guard_act_pos_or

        else:
            # if item_act != 'X':
            #     total += 1
            matrix[guard_act_pos[0]][guard_act_pos[1]] = 'X'
            guard_prev_pos = guard_act_pos
            guard_act_pos = get_new_pos(guard_act_pos, guard_act_dir)
        
        imprimir_matriz(matrix, guard_act_pos, guard_act_dir)
    return False

if __name__ == '__main__':    
    guard_act_pos = guard_ini_pos
    guard_prev_pos = guard_act_pos
    guard_act_dir = UP
    # (i,j)
    result = calculate_path(guard_act_pos, guard_prev_pos, guard_act_dir, False, None, matrix)

    print(TOTAL)