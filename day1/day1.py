def calibrateLine(line):
    nums_as_strings = {"one": "one", "two": "two", "three": "three", 
                       "four": "four", "five":"five", "six":"six", 
                       "seven":"seven", "eight":"eight", "nine":"nine"}
    firstNum = ""
    lastNum = ""
    possible_string_num = ""
    for char in line: 
        if char.isnumeric() and firstNum == "": 
            firstNum = char 
            possible_string_num = ""
        elif char.isnumeric() and firstNum != "": 
            lastNum = char 
            possible_string_num = ""
        elif char.isnumeric() == False: 
            possible_string_num += char 
            if possible_string_num in nums_as_strings.values():
                #matches 

    num_str = ""
    if lastNum == "" and firstNum != "":
        num_str = firstNum + firstNum 
    elif lastNum != "" and firstNum != "":
        num_str = firstNum + lastNum
    else:
        #No number, skip line
        num_str = "0"

    print("Num: ", int(num_str))
    return int(num_str)
    
def calibrate(filename):
    file = open(filename, "r") 

    sum = 0
    while True: 
        line = file.readline() 

        if not line: 
            break 
        line = line.strip() 

        sum += calibrateLine(line)
        

    print("Sum: ", sum)
    file.close()

if __name__ == "__main__": 
    "Calibrating..."
    calibrate("dataset1.txt")