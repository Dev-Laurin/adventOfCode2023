def countEngineParts(filename):
    file = open(filename, "r") 

    #Find symbol and number positions
    symbol_pos = []
    number_pos = []
    index = 0 
    STATE = ""
    num_str = ""
    num_indices = []
    touching_pos = []
    while True: 
        line = file.readline() 

        if not line: 
            break 
        line = line.strip() 
        parseLine(line, symbol_pos, number_pos, 
                  index, STATE, num_str, num_indices, touching_pos)

    sum = sumTouchingNumbers(touching_pos, number_pos)
        
    print("Sum:", sum)
    file.close()

def sumTouchingNumbers(touchingPositions, number_pos):
    #Calculate which numbers touch a symbol
    number_list = calculateTouchingNumbers(touchingPositions, number_pos)
    
    sum = 0
    for num in number_list: 
        sum += int(num)
    return sum 


def calculateTouchingPositions(line, symbol_pos, touching_positions):
    length = len(line)
    lastIndex = length - 1
    for s_pos in symbol_pos: 
        if calculateIfValid(s_pos - length, lastIndex):
            #Up
            touching_positions.append(s_pos - length)
        if calculateIfValid(s_pos + length, lastIndex):
            #Down
            touching_positions.append(s_pos + length)
        if calculateIfValid(s_pos - 1, lastIndex):
            #Left
            touching_positions.append(s_pos - 1)
        if calculateIfValid(s_pos + 1, lastIndex):
            #Right
            touching_positions.append(s_pos + 1)
        if calculateIfValid(s_pos - length + 1, lastIndex):
            #Upper Right Diagonal
            touching_positions.append(s_pos - length + 1)
        if calculateIfValid(s_pos - length - 1, lastIndex):
            #Upper Left Diagonal
            touching_positions.append(s_pos - length - 1)
        if calculateIfValid(s_pos + length + 1, lastIndex):
            #Lower Right Diagonal
            touching_positions.append(s_pos + length + 1)
        if calculateIfValid(s_pos + length - 1, lastIndex):
            #Lower Left Diagonal
            touching_positions.append(s_pos + length - 1)

def calculateIfValid(position, lastIndex): 
    if position < 0 or position > lastIndex: 
        return False 
    return True 

def calculateTouchingNumbers(positions, number_positions):
    num_list = []

    print("positions: ", positions)
    print("num pos:",number_positions)

    for p in positions: 
        print("Position: ", p)
        for index, num in enumerate(number_positions): 
            print("number_list num:", num, "index:", index)
            for num_pos in number_positions[index][1]:
                print("number position: ", num_pos)
                if num_pos == p: 
                    print("number touches a symbol")
                    num_list.append(number_positions[index][0])

    return num_list 

def parseLine(line, symbol_pos, number_pos, index, STATE, num_str, num_indices, touching_pos):
    #Find symbol and number positions
    for char in line: 
        #A Symbol is not a period and not a number
        if char == ".":
            if STATE == 'NUM': 
                number_pos.append([num_str, num_indices])
                num_str = ""
            STATE = 'PERIOD'
            index += 1 
            continue 
        try: 
            int(char)
            STATE = 'NUM'
            num_str += char 
            num_indices.append(index)
            index += 1 
            continue 
        except: 
            if STATE == 'NUM': 
                number_pos.append([num_str, num_indices])
                num_str = ""
            STATE = 'SYMBOL'
            num_str = ""
            symbol_pos.append(index) 
        
        index += 1 

    #Calculate touching symbol positions
    calculateTouchingPositions(line, symbol_pos, touching_pos)


if __name__ == "__main__": 
    print("Accounting for Engine Parts...")
    countEngineParts("dataset.txt")