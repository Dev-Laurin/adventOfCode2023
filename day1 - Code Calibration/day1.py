def calibrateLine(line):
    nums_as_strings = {"one": "1", "two": "2", "three": "3", 
                       "four": "4", "five": "5", "six": "6", 
                       "seven": "7", "eight": "8", "nine": "9"}
    firstNum = ""
    lastNum = ""
    firstNumIndex = len(line) - 1
    lastNumIndex = 0 
    currentIndex = 0

    for char in line: 
        try: 
            integer = int(char)
            if integer and firstNum == "": 
                firstNum = char 
                firstNumIndex = currentIndex
            if integer and firstNum != "": 
                lastNum = char 
                lastNumIndex = currentIndex
            currentIndex += 1
        except: 
            currentIndex += 1

    #is lettered word before or after? 
    for number_string in nums_as_strings: 
        try: 
            index = line.index(number_string)
            #First occurrence 
            if index >= 0: 
                if index <= firstNumIndex:
                    firstNum = nums_as_strings[number_string]
                    firstNumIndex = index

            #Last occurrence
            index = line.rfind(number_string)
            if index >= 0: 
                if index >= lastNumIndex: 
                    lastNum = nums_as_strings[number_string]
                    lastNumIndex = index 

        except: 
            continue
        
    num_str = ""
    if lastNum == "" and firstNum != "":
        num_str = firstNum + firstNum 
    elif lastNum != "" and firstNum != "":
        num_str = firstNum + lastNum
    else:
        #No number, skip line
        num_str = "0"

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
    print("Calibrating...")
    calibrate("dataset1.txt")