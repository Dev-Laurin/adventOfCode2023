def calibrateLine(line):
    firstNum = ""
    lastNum = ""
    for char in line: 
        if char.isnumeric() and firstNum == "": 
            firstNum = char 
        elif char.isnumeric() and firstNum != "": 
            lastNum = char 

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