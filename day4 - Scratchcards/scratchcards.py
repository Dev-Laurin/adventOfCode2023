import copy 

def tallyPoints(filename): 
    file = open(filename, "r") 

    cards = {}
    while True: 
        line = file.readline() 

        if not line: 
            break 
        line = line.strip() 
        parseLine(line, cards)

    cardsProcessed = processScratchCards(cards)
    
    print("Total Scratchcards:", cardsProcessed)
    file.close()
    return cardsProcessed

def processScratchCards(cards):
    cards_processed = 0 
    cards_to_process = []


    #Populate initial cards to process
    for card in cards.keys():     
        cards_to_process.append(card)

    #Process all cards, including copies until done
    while len(cards_to_process) > 0: 
        for card_id in cards_to_process:
            won_nums = []
            print("CardID:", card_id)

            for win_num in cards[card_id]["winning_nums"]: 
                if win_num in cards[card_id]["your_nums"]: 
                    won_nums.append(win_num)

            cards_to_process.remove(card_id)

            cards_processed += 1

            print("cards left to be processed:", len(cards_to_process))

            if len(won_nums) > 0: 
                #copy other cards
                for i in range(1, len(won_nums) + 1):
                    cardCopy = int(card_id) + i
                    print("Adding copy:", cardCopy)
                    cards_to_process.append(cardCopy)

    return cards_processed 

def parseLine(line, cards):
    semiIndex = line.find(":")
    cardNum = line[5:semiIndex]
    startIndex = semiIndex + 2
    stripped_line = line[startIndex:]

    STATE = "WINNING_NUMS"
    current_num_str = ""
    winning_nums = {}
    your_nums = {}
    for char in stripped_line: 
        if char == "|":
            STATE = "YOUR_NUMS"
            continue 
        elif char == " ": 
            if current_num_str != "": 
                current_num_str = int(current_num_str)
                if STATE == "WINNING_NUMS":
                    winning_nums[current_num_str] = current_num_str
                elif STATE == "YOUR_NUMS":
                    your_nums[current_num_str] = current_num_str
                current_num_str = ""
            continue 
        elif STATE == "WINNING_NUMS" or STATE == "YOUR_NUMS": 
            current_num_str += char 

    current_num_str = int(current_num_str)
    your_nums[current_num_str] = current_num_str

    cards[int(cardNum.strip())] = {"winning_nums": winning_nums, "your_nums": your_nums}

def calculatePoints(cards): 
    won_nums = []
    for card in cards.values():
        for win_num in card["winning_nums"]: 
            if win_num in card["your_nums"]: 
                won_nums.append(win_num)

    points = 0 
    numbers_won = len(won_nums)

    if numbers_won == 1: 
        points = 1
    elif numbers_won > 1: 
        points = 1 
        for i in range(1, numbers_won): 
            points *= 2 

    return points 

if __name__ == "__main__": 
    print("Tallying Scratchcards...")
    tallyPoints("dataset.txt")