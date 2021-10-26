# Initiate a dictionary to convert the character-based cards to numbers
decode_cards = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "T" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14
}

#The function initiates 2 lists for each of the hands. The numbers & the suits are kept in separate sublists
def split_hands (line):
    hand_1 = [[],[]]
    hand_2 = [[],[]]
    line = line.strip()
    split_1 = line[0:15].replace(" ","")
    for i in range(len(split_1)):
        if i % 2 == 0:
            card_number = decode_cards.get(split_1[i])
            hand_1[0].append(card_number)
        else:
            hand_1[1].append(split_1[i])
    #print(hand_1)
    split_2 = line[15:30].replace(" ","")
    for i in range(len(split_2)):
        if i % 2 == 0:
            card_number = decode_cards.get(split_2[i])
            hand_2[0].append(card_number)
        else:
            hand_2[1].append(split_2[i])
    #print(hand_2)
    return hand_1, hand_2

#Function to evaluate the card of each player. It will return the status & an ordered list of the player's cards

def card_evaluation(hand):

    #Initiate a dictionary to allow us to evaluate the player's hand
    status = {
        "Royal_Flush" : None,
        "Straight_Flush" : None,
        "Four_of_a_kind" : None,
        "Full_house" : None,
        "Flush" : None,
        "Straight" : None,
        "Three_of_a_kind" : None,
        "Two_pairs" : None,
        "One_pair" : None,
        "High_card" : None
    }

    #Evaluate whether cards are of the same suit
    for card in hand[1]:
        if card != hand[1][0]:
            status["Flush"] = None
            break
        status["Flush"] = 6

    counter = []
    for card in hand[0]:
        counter.append(hand[0].count(card))

    #Evaluate whether there is a "straight", and additional conditions for "Straight Flush" and "Royal Flush"
    hand[0].sort()
    if (hand[0][-1] - hand[0][0] == 4) and (max(counter) == 1):
        status["Straight"]  = 5
        if (status["Straight"] == 5) & (status["Flush"] == 6):
            if hand[0][-1] == 14:
                status["Royal_Flush"] = 10
            else:
                status["Straight_Flush"] = 9

    #Evaluate the number of same cards on player's hand
    counter = []
    for card in hand[0]:
        counter.append(hand[0].count(card))
    if max(counter) == 4:
        status["Four_of_a_kind"] = 8
        for measure in counter:
            if measure == 1:
                 temp = hand[0].pop(counter.index(measure))
                 hand[0].append(temp)

    elif max(counter) == 3 and min(counter) == 2:
        status["Full_house"] = 7
        for measure in counter:
            if measure == 2:
                 temp = hand[0].pop(counter.index(measure))
                 hand[0].append(temp)

    elif max(counter) == 3 and min(counter) == 1:
        status["Three_of_a_kind"] = 4
        temp = []
        for measure in counter:
            if measure == 3:
                temp.append(hand[0].pop(counter.index(measure)))
        hand[0].sort(reverse=True)
        for number in temp:
            hand[0].insert(0,number)

    elif max(counter) == 2 and counter.count(2) == 4:
        status["Two_pairs"] = 3
        temp = []
        for element in counter:
            if element == 1:
                temp.append(hand[0].pop(counter.index(element)))
        hand[0].sort(reverse = True)
        for number in temp:
            hand[0].append(number)

    elif max(counter) == 2 and counter.count(2) == 2:
        status["One_pair"] = 2
        temp = []
        for element in counter:
            if element == 2:
                temp.append(hand[0].pop(counter.index(element)))
        hand[0].sort(reverse = True)
        for number in temp:
            hand[0].insert(0,number)
    else:
        High_card = hand[0][-1]
        status["High_card"] = 1
        hand[0].sort(reverse = True)

    #For loop to go through the dictionary and return the hand status & the ordered list of the player's hand
    for play in status:
        if status[play] != None:
            return(status[play], hand[0])
            break

player1_wins = 0
player2_wins = 0
game_no = 0
with open('p054_poker.txt') as poker_file:
    for line in poker_file:
        game_no += 1
        hand_1, hand_2 = split_hands(line)
        status_player1, cards_player1 = card_evaluation(hand_1)
        status_player2, cards_player2 = card_evaluation(hand_2)
        print("GAME No :", game_no)
        print("---------------------------------------------------------------")
        print("Player one has scored:", status_player1, "and his cards are the following: ", cards_player1)
        print("Player two has scored:", status_player2, "and his cards are the following: ", cards_player2)
        if status_player1 < status_player2:
            print("PLAYER 2 WINS!\n")
            player2_wins +=1
            continue
        elif status_player1 > status_player2:
            print("PLAYER 1 WINS!\n")
            player1_wins += 1
        elif status_player1 == status_player2:
            if cards_player1 > cards_player2:
                print("PLAYER 1 WINS!\n")
                player1_wins +=1
            else:
                player2_wins +=1
                print("PLAYER 2 WINS!\n")
print(player1_wins)
