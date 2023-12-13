def tallyPoints(filename): 
    file = open(filename, "r") 

    sum = 0
    while True: 
        line = file.readline() 

        if not line: 
            break 
        line = line.strip() 
        cards = {}
        parseLine(line, cards)
        sum += calculatePoints(cards)
        
    print("Sum:", sum)
    file.close()

def parseLine(line, cards):
    semiIndex = line.find(":")
    cardNum = line[5:semiIndex]
    startIndex = semiIndex + 2
    stripped_line = line[startIndex:]

    print("stripped_line:", stripped_line)

    STATE = "WINNING_NUMS"
    PARSE_STATE = "START"
    current_num_str = ""
    winning_nums = {}
    your_nums = {}
    for char in stripped_line: 
        print("ChAR: ",char)
        if char == "|":
            STATE = "YOUR_NUMS"
            continue 
        elif char == " ": 
            if current_num_str != "": 
                if STATE == "WINNING_NUMS":
                    winning_nums[current_num_str] = current_num_str
                elif STATE == "YOUR_NUMS":
                    your_nums[current_num_str] = current_num_str
                current_num_str = ""
            continue 
        elif STATE == "WINNING_NUMS" or STATE == "YOUR_NUMS": 
            current_num_str += char 

    your_nums[current_num_str] = current_num_str

    cards[cardNum] = {"winning_nums": winning_nums, "your_nums": your_nums}
    print(cards)

def calculatePoints(cards): 
    won_nums = []
    print(cards)
    for card in cards.values():
        print("Card:", card) 
        for win_num in card["winning_nums"]: 
            if win_num in card["your_nums"]: 
                won_nums.append(win_num)

    print("your winning nums!", won_nums)
    points = 0 
    numbers_won = len(won_nums)
    print(numbers_won)
    if numbers_won == 1: 
        points = 1
    elif numbers_won > 1: 
        points = 1 
        for i in range(1, numbers_won): 
            points *= 2 
    print("Points:", points)
    return points 

if __name__ == "__main__": 
    print("Accounting for Engine Parts...")
    tallyPoints("dataset.txt")