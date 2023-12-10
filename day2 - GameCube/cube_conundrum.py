
def calculateCube(filename, red_cube_num, green_cube_num, blue_cube_num):
    file = open(filename, "r") 

    sum = 0
    while True: 
        line = file.readline() 

        if not line: 
            break 
        line = line.strip() 

        allowed_maximums = {"red": red_cube_num, "green": green_cube_num, 
                            "blue": blue_cube_num}
        sum += calculateLine(line, allowed_maximums)
        
    print("Sum: ", sum)
    file.close()

def calculateLine(line, allowed_maximums):
    #Get the Game ID 
    stripped_line = line.replace(" ", "")
    colon_index = stripped_line.index(":")
    game_id = stripped_line[4:colon_index]
    stripped_line = stripped_line[6:]

    #Find max of each color 
    maximums = {"red": 0, "blue": 0, "green": 0}
    num = ""
    STATE = ""
    for char in stripped_line: 
        try: 
            int(char)
            STATE = 'NUM'
            num += char 
        except: 
            if char == "b":
                STATE = 'BLUE'
            elif char == "g": 
                STATE= 'GREEN'
            elif char == "," or char == ";": 
                STATE = 'PUNCT'
                continue 
            
            if char == "d": 
                maximums["red"] = max(int(num), maximums["red"])
                num = ""
                STATE = ""
            elif char == "n": 
                maximums["green"] = max(int(num), maximums["green"])
                num = ""
                STATE = ""

            elif char == "e" and STATE == "BLUE": 
                maximums["blue"] = max(int(num), maximums["blue"])
                num = ""
                STATE = ""
                
    if (maximums["red"] <= allowed_maximums["red"] and 
    maximums["green"] <= allowed_maximums["green"] and 
    maximums["blue"] <= allowed_maximums["blue"]): 
        return int(game_id)
    
    return 0


if __name__ == "__main__": 
    print("Calibrating...")
    calculateCube("dataset1.txt", 12, 13, 14)