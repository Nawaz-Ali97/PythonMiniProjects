import random
playerIn=True
dealerIn=True
#Deck of cards 
deck =[2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A',  'J', 'Q', 'K', 'A',  'J', 'Q', 'K', 'A']
playerhand =[]
dealerhand = []

#deal the cards
def dealCard(turn):
    card =random.choice(deck)
    turn.append(card)
    deck.remove(card)


#calculate the totals
def total(turn):
    total = 0
    face = [ 'J', 'Q', 'K']
    for card in turn:
        if card in range (1,11):
            total += card
        elif card in face:
            total +=10
        else:
            if total >11:
                total +=1
            else:
                total +=11
    return total
            

#check for winner
def revealDealerHand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand [1]
    


#loop
for _ in range(2):
    dealCard(dealerhand)
    dealCard(playerhand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X" )
    print(f"You have {playerhand} for a total of {total(playerhand)}")
    if playerIn:
        stayOrHit = input("1 to Stay\n2 to Hit\n")
    if total(dealerhand)>16:
        dealerIn=False
    else:
        dealCard(dealerhand)
    if stayOrHit == '1':
        playerIn = False    
    else:
        dealCard(playerhand)
    if total(playerhand) >= 21:
        break
    elif total(dealerhand)>=21:
        break

if total(playerhand) == 21:
    print(f"\nYou have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Blackjack! You win!")
elif total(dealerhand) ==21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Blackjack! Dealer wins!")
elif total(playerhand) > 21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You Bust! Dealer wins!")
elif total(dealerhand) >21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Dealer Busts! You win!")
elif 21 - total(dealerhand) < 21 - total(playerhand):
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Dealer wins!")
elif 21 - total(dealerhand) > 21 - total(playerhand):
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You win!")