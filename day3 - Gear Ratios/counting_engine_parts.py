def countEngineParts(filename):
    file = open(filename, "r") 

    sum = 0
    while True: 
        line = file.readline() 

        if not line: 
            break 
        line = line.strip() 
        sum += parseLine(line)
        
    print("Sum:", sum)
    file.close()

def calculateTouchingPositions(position, lineSize):


def parseLine(line):
    #Find symbol positions 
    symbol_pos = []
    index = 0 
    for char in line: 
        #A Symbol is not a period and not a number
        if char == ".":
            index += 1 
            continue 
        try: 
            int(char)
            index += 1 
            continue 
        except: 
            symbol_pos.append(index) 
        
        index += 1 

    #Calculate touching symbol positions
    length = len(line)
    touching_positions = []
    for s_pos in symbol_pos: 
        #Up
        touching_positions.push(s_pos - length)
        #Down
        touching_positions.push(s_pos + length)
        #Left
        touching_positions.push(s_pos - 1)
        #Right
        touching_positions.push(s_pos + 1)
        #Upper Right Diagonal
        touching_positions.push(s_pos - length + 1)
        #Upper Left Diagonal
        touching_positions.push(s_pos - length - 1)
        #Lower Right Diagonal
        touching_positions.push(s_pos + length + 1)
        #Lower Left Diagonal
        touching_positions.push(s_pos + length - 1)

    #Find number positions 
    

    return 0 

if __name__ == "__main__": 
    print("Accounting for Engine Parts...")
    countEngineParts("dataset.txt")