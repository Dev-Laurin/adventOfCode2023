def countEngineParts(filename):
    file = open(filename, "r") 

    #Find symbol and number positions
    symbol_pos = []
    number_pos = []
    index = 0 
    STATE = ""
    num_str = ""
 
    string = file.read()
    if not string: 
        return  
    lineLength = string.find("\n")
    string = string.replace("\n", "")
    
    parseFile(string, symbol_pos, number_pos, 
                index, STATE, num_str, lineLength)

    sum = sumTouchingNumbers(symbol_pos, number_pos)
    print("Sum:", sum)
    file.close()

    return sum 

def calculateGearRatio(li):
    gearRatio = 1 
    for num in li: 
        gearRatio *= num 
    return gearRatio 

def sumTouchingNumbers(touchingPositions, number_pos):
    #Calculate which numbers touch a symbol
    calculateTouchingNumbers(touchingPositions, number_pos)

    sum = 0
    for sym in touchingPositions: 
        if len(sym[2]) > 1: 
            sum += calculateGearRatio(sym[2]) 

    return sum 


def calculateTouchingPositions(data, s_pos, length):
    lastIndex = len(data)
    up = s_pos - length
    down = s_pos + length
    left = s_pos - 1
    right = s_pos + 1
    upper_right = s_pos - length + 1
    upper_left = s_pos - length - 1
    lower_right = s_pos + length + 1
    lower_left = s_pos + length - 1

    touching_positions = {}
    if calculateIfValid(up, lastIndex):
        #Up
        touching_positions[up] = up 
    if calculateIfValid(down, lastIndex):
        #Down
        touching_positions[down] = down 
    if calculateIfValid(left, lastIndex):
        #Left
        touching_positions[left] = left 
    if calculateIfValid(right, lastIndex):
        #Right
        touching_positions[right] = right 
    if calculateIfValid(upper_right, lastIndex):
        #Upper Right Diagonal
        touching_positions[upper_right] = upper_right 
    if calculateIfValid(upper_left, lastIndex):
        #Upper Left Diagonal
        touching_positions[upper_left] = upper_left
    if calculateIfValid(lower_right, lastIndex):
        #Lower Right Diagonal
        touching_positions[lower_right] = lower_right
    if calculateIfValid(lower_left, lastIndex):
        #Lower Left Diagonal
        touching_positions[lower_left] = lower_left

    return touching_positions

def calculateIfValid(position, lastIndex): 
    if position < 0 or position > lastIndex: 
        return False 
    return True 

def calculateTouchingNumbers(positions, number_positions):
    #TODO, refactor
    for sym_index, sym in enumerate(positions):
        for num_index, num in enumerate(number_positions): 
            for n in num[1]: 
                if n in sym[1] and number_positions[num_index][2] != "checked":
                    positions[sym_index][2].append(int(number_positions[num_index][0]))
                    number_positions[num_index][2] = "checked"
                    break 


def parseFile(data, symbol_pos, number_pos, index, STATE, num_str, length):
    #Find symbol and number positions
    num_indices = {}
    for char in data: 
        #A Symbol is not a period and not a number
        if char == ".":
            if STATE == 'NUM': 
                number_pos.append([num_str, num_indices, "unchecked"])
                num_str = ""
                num_indices = {}
            STATE = 'PERIOD'
            index += 1 
            continue 
        try: 
            int(char)
            STATE = 'NUM'
            num_str += char 
            num_indices[index] = index
            index += 1 
            continue 
        except: 
            if STATE == 'NUM': 
                number_pos.append([num_str, num_indices, "unchecked"])
                num_str = ""
                num_indices = {}
            symbol_pos.append([char, calculateTouchingPositions(data, index, length), []])
            STATE = 'SYMBOL'
            num_str = ""
        
        index += 1 

if __name__ == "__main__": 
    print("Accounting for Engine Parts...")
    countEngineParts("dataset.txt")