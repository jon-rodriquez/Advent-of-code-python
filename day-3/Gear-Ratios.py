def read_file(filename):
    file = open(filename)
    file_arr = []

    for line in file:
        file_arr.append(list(line.strip()))

    return file_arr

def is_special_charater(c):
    return not c.isdigit() and c != "."

def has_adjacent(matrix, row, left, right) -> bool:
    for i in range(left, right+1):
        if i == left:
            #check left
            if left-1>=0 and is_special_charater(matrix[row][left-1]):
                return True
            #check upleft
            if left-1>=0 and row-1>=0 and is_special_charater(matrix[row-1][left-1]):
                return True
            #check downleft
            if row+1<len(matrix) and left-1>=0 and is_special_charater(matrix[row+1][left-1]):
                return True

        if i == right:
            #check right
            if right+1<len(matrix[row]) and is_special_charater(matrix[row][right+1]):
                return True
            #check upright
            if right+1<len(matrix[row]) and row-1>=0 and is_special_charater(matrix[row-1][right+1]):
                return True
            #check downright
            if row+1<len(matrix) and right+1<len(matrix[row]) and is_special_charater(matrix[row+1][right+1]):
                return True

        #check up
        if row-1>=0 and is_special_charater(matrix[row-1][i]):
            return True
        #check down
        if row+1<len(matrix) and is_special_charater(matrix[row+1][i]):
            return True

       
    return False

def determine_sum():
    engine_matrix = read_file("./input.txt")

    sum = 0

    for i, line in enumerate(engine_matrix):
        temp_number = ""
        for k, charater in enumerate(line):
            if charater.isdigit():
                temp_number+=charater

            end_of_num_not_end = charater.isdigit() and k+1 < len(line) and not line[k+1].isdigit()
            end_of_num_end_line = charater.isdigit() and k+1 == len(line)

            if end_of_num_not_end or end_of_num_end_line:
        #then search for all adjacent spaces for a symbol
                if has_adjacent(engine_matrix, i, k-len(temp_number)+1, k):
                    sum+=int(temp_number)
                temp_number = ""
    print(sum)

determine_sum()
