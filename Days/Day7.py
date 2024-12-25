from utils.get_data import *

def get_rows(data):
    rows = []
    for row in data:
        if row == '': continue
        row = row.replace(':', '')
        row = row.split(' ')
        row = [int(num) for num in row]
        rows.append(row)
    return rows

def is_combination_possible(row, partial_result, i) -> int:
    #Returns the target number if combinaton possible, 0 else.
    if partial_result == row[0] and i == len(row):
        return row[0]
    
    if i >= len(row):
        return 0
    
    for operation in ['+', '*', '||']:
        original_partial_result = partial_result
        
        #Try sum
        if partial_result == 0: partial_result = row[i] 
        elif operation == '+':
            partial_result += row[i]
        elif operation == '*':
            partial_result *= row[i]
        elif operation == '||':
            partial_result = int(str(partial_result) + str(row[i]))
        
        result = is_combination_possible(row, partial_result, i + 1)

        if result != 0:
            return result

        partial_result = original_partial_result

    return 0

if __name__ == '__main__':    
    data = get_data(7)
    # data = read_from_file()
    data = data.split('\n')

    rows = get_rows(data)

    total = 0

    for row in rows:
        res = is_combination_possible(row, 0, 1)
        if res != 0:
            total += res
            # print(row)
    

print(total)




