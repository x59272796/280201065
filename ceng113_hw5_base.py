import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

    def get_tip(self, tip):
      # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
      # where * indicates optionality and tip is either a value or a color.
      # e.g. "1,2,w" or "2,3" or "1,2,3,2"
      # output: none
      # The tip is processed and the information about the bot's hand is updated.
      tip.split(",")
      value = tip.pop()
      if value.isalpha() :
        for index in range(len(tip) - 1) :
          self.hand()[tip[index]][0] = value
      else :
        for index in range(len(tip) - 1) :
            self.hand()[tip[index]][1] = value

    def update_count_deck(self,card):
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.
        self.count_deck().remove(card) 

    def update_hand(self,num):
        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.
        self.hand().pop(num - 1)
        self.hand().append(self.count_deck.pop(0))  # i append the card at the top of the deck, like how it would work in real life.

    def give_tip(self):
        # input: none
        # output: a string created by the bot in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # The bot checks the player's hand and finds a good tip to give. Minimal requirement for this
        # function is that bot gives the tip for maximum possible number of cards.
        # BONUS: Smarter decision-making algorithms can be implemented.
        tip = ""
        mostRepeated = getMostRepeated(self.play_hand())
        blackList = []
        whiteList = []
        for card in self.play_hand() :
          if card[0] == "b" :
            blackList.append([self.play_hand().index(card), card])
          else :
            whiteList.append([self.play_hand().index(card), card])
        if len(blackList) > len(mostRepeated) and len(blackList) > len(whiteList) :
          for card in blackList :
            tip += str(card[0] + 1) + ","
          tip += "b"
        elif len(whiteList) > len(mostRepeated) and len(whiteList) > len(blackList) :
          for card in whiteList :
            tip += str(card[0] + 1) + ","
          tip += "w"
        else :
          for card in mostRepeated :
            tip += str(card[0]) + ","
          tip += str(mostRepeated[0][1][1])
        
    def pick_stack(self):
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
        found = False
        location = -1
        for stacks in stack :
          for card in self.hand() :
            if card[0] == stacks[-1][0] and card[1] > stacks[-1][1] :
              location = self.hand().index(card)
              found = True
              break
          if found :
            break
    

    def pick_discard(self):
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.
        card2discard = []
        for card in self.hand() :
          if card in self.stack() :
            card2discard = card
            break
          elif card == ["!",-1] :
            card2discard = card
        return card2discard

def shuffle(deck):
  # input: deck to be shuffled
  # output: none
  # shuffle the deck
  # you are free to choose the algorithm you want
  # explain your shuffle algorithm in a comment
  # first i copy the original deck to a temporary deck, then clear the original deck, then append each card randomly from the temporary deck to the original deck, therefore ending up with a shuffled deck.
  tempDeck = list(deck)
  print(id(deck), id(tempDeck))
  deck.clear()
  for x in range(len(tempDeck)) :
    deck.append(tempDeck.pop(random.randint(0, len(tempDeck) - 1)))

def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")

def update_hand(hand,deck,num):
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.
    removedCard = hand.pop(num - 1)
    if len(deck) > 0 :
      hand.append(deck.pop(0))
    return removedCard

def try_stack(card,stack,trash,lives):
    # input: the card to be stacked, current stack, current trash, number of lives
    # output: updated number of lives
    # This function tries to place the card in the stack. If successful, the card is appropriately
    # added to the stack and the updated stack is printed. Otherwise, the card is appended to the
    # trash, the trash is sorted for better viewing and number of lives is decreased by 1. A warning
    # and the current number of lives are printed.
    if card[0] == "b" : # index determines which stack (black or white) to stack on depending on the card color.
      index = 1
    else :
      index = 0
    if len(stack[index]) == 0 :
      stack.append(card)
      print("The current stack is: " + str(stack))
    elif stack[index][-1][1] < card[1] :
      stack.append(card)
      print("The current stack is: " + str(stack))
    else :
      trash.append(card)
      trash.sort()
      lives -= 1
      print("Stacking unsuccessful. Remaining lives: " + str(lives))
    return lives

def discard(card,trash,tips):
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.
    trash.append(card)
    trash.sort()
    tips += 1
    print("The trash is: " + str(trash))
    print("Remaining tips:" + str(tips))

def getMostRepeated(sampleList) :
  frequency = {}
  for element in sampleList :
    if element[1] not in frequency.keys() :
      frequency[element[1]] = 1
    else :
      frequency[element[1]] += 1
  maxValue = max(frequency.values())
  mostRepeated = []
  for element in sampleList :
    if frequency[element[1]] == maxValue :
      mostRepeated.append([sampleList.index(element), element])
      value = element[1]
  return mostRepeated

print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck)
# First hands are dealt.
comp_hand = deck[0], deck[1], deck[2]  # i gave the first 3 cards to the ai. (# TODO: obtain cards (3 cards) from deck)
play_hand = deck[3], deck[4], deck[5] # i gave the next three to the player. # TODO: obtain cards (3 cards) from deck
del deck[0:6]
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:", comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                turn = 1        # Switch turns.
                # Take a tip from the player, give it to the bot, update and print the number of tips.
                tip = str(input("Write the tip.").split(",")  
                while len(tip) < 2 or len(tip) > 4 or not tip[-1].isalnum() :
                  tip = str(input("Write the tip properly again.").split(",")
                bot.get_tip(tip)
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            turn = 1        # Switch turns.
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
            pass
        elif inp == "d":
            turn = 1        # Switch turns.
            # Take the location of the card to be discarded from the player,
            # update hands and bot's count_deck and discard the selected card.
            pass
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        if tips > 1  and len(play_hand)>0:
            # Take a tip from the bot. Update the number of tips. Print both
            # the given tip by the bot and the updated number of tips.
            pass
        else:
            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck
            # and discard the selected card.
            pass
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives==0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break

