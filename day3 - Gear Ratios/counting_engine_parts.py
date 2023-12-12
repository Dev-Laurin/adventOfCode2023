def countEngineParts(filename):
    file = open(filename, "r") 

    #Find symbol and number positions
    symbol_pos = []
    number_pos = []
    index = 0 
    STATE = ""
    num_str = ""
    touching_pos = []
 
    string = file.read()
    if not string: 
        return  
    lineLength = string.find("\n")
    string = string.replace("\n", "")
    
    parseFile(string, symbol_pos, number_pos, 
                index, STATE, num_str, touching_pos, lineLength)
    
    print("Touching Pos:", touching_pos)

    sum = sumTouchingNumbers(touching_pos, number_pos)
        
    print("Sum:", sum)
    file.close()

    return sum 

def sumTouchingNumbers(touchingPositions, number_pos):
    #Calculate which numbers touch a symbol
    number_list = calculateTouchingNumbers(touchingPositions, number_pos)
    print("Numbers to sum: ", number_list)
    sum = 0
    for num in number_list: 
        sum += int(num)
    return sum 


def calculateTouchingPositions(data, symbol_pos, touching_positions, length):
    lastIndex = len(data)
    print("lastIndex: ", lastIndex)
    print("length: ", length)
    for s_pos in symbol_pos: 
        up = s_pos - length
        down = s_pos + length
        left = s_pos - 1
        right = s_pos + 1
        upper_right = s_pos - length + 1
        upper_left = s_pos - length - 1
        lower_right = s_pos + length + 1
        lower_left = s_pos + length - 1
        if calculateIfValid(up, lastIndex):
            #Up
            touching_positions.append(up)
        if calculateIfValid(down, lastIndex):
            #Down
            touching_positions.append(down)
        if calculateIfValid(left, lastIndex):
            #Left
            touching_positions.append(left)
        if calculateIfValid(right, lastIndex):
            #Right
            touching_positions.append(right)
        if calculateIfValid(upper_right, lastIndex):
            #Upper Right Diagonal
            touching_positions.append(upper_right)
        if calculateIfValid(upper_left, lastIndex):
            #Upper Left Diagonal
            touching_positions.append(upper_left)
        if calculateIfValid(lower_right, lastIndex):
            #Lower Right Diagonal
            touching_positions.append(lower_right)
        if calculateIfValid(lower_left, lastIndex):
            #Lower Left Diagonal
            touching_positions.append(lower_left)

def calculateIfValid(position, lastIndex): 
    print("checking if position is valid: ", position, " lastIndex: ", lastIndex)
    if position < 0 or position > lastIndex: 
        return False 
    return True 

def calculateTouchingNumbers(positions, number_positions):
    num_list = []

    print("positions: ", positions)
    print("num pos:", number_positions)

    for p in positions: 
        #print("Position: ", p)
        for index, num in enumerate(number_positions): 
            #print("number_list num:", num, "index:", index)
            for num_pos in number_positions[index][1]:
                #print("number position: ", num_pos)
                if num_pos == p and number_positions[index][2] != "checked": 
                    #print("number touches a symbol")
                    number_positions[index][2] = "checked"
                    num_list.append(number_positions[index][0])
                    break 

    return num_list 

def parseFile(data, symbol_pos, number_pos, index, STATE, num_str, touching_pos, length):
    #Find symbol and number positions
    num_indices = []
    for char in data: 
        #A Symbol is not a period and not a number
        if char == ".":
            if STATE == 'NUM': 
                number_pos.append([num_str, num_indices, "unchecked"])
                num_str = ""
                num_indices = []
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
                number_pos.append([num_str, num_indices, "unchecked"])
                num_str = ""
                num_indices = []
            STATE = 'SYMBOL'
            print("Symbol found:", char, "at index:", index)
            num_str = ""
            symbol_pos.append(index) 
        
        index += 1 

    print("Symbol positions:", symbol_pos)

    #Calculate touching symbol positions
    calculateTouchingPositions(data, symbol_pos, touching_pos, length)

    print("Symbol positions:", symbol_pos)


if __name__ == "__main__": 
    print("Accounting for Engine Parts...")
    countEngineParts("dataset.txt")