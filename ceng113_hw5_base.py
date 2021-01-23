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

        self.known_play_hand = [['!',-1],['!',-1],['!',-1]] # this is the attribute i introduced, it will help coming up with new tips. it represents the player hand as the player knows

    def get_tip(self, tip):
      # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
      # where * indicates optionality and tip is either a value or a color.
      # e.g. "1,2,w" or "2,3" or "1,2,3,2"
      # output: none
      # The tip is processed and the information about the bot's hand is updated.

      # my approach takes the tip, pops the last element which is the value the previous cards had, and updates bots hand accordingly.
      value = tip.pop()
      if value.isalpha() :
        for number in tip :
          self.hand[int(number) - 1][0] = value
      else :
        value = int(value)
        for number in tip :
          self.hand[int(number) - 1][1] = value

    def update_count_deck(self,card):
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.
        self.count_deck.remove(card) 

    def update_hand(self,num): 
        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.

        # updates bots hand as it knows
        self.hand.pop(num - 1)
        if len(self.count_deck) > 3 : # 3 because bot may has these 3 cards
          self.hand.append(["!", -1])
        

    def give_tip(self):
        # input: none
        # output: a string created by the bot in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # The bot checks the player's hand and finds a good tip to give. Minimal requirement for this
        # function is that bot gives the tip for maximum possible number of cards.
        # BONUS: Smarter decision-making algorithms can be implemented.

        # what this function does is it gets the number of same numbered cards with getMostRepeated function ive implemented, and it gets the number of cards with the same color. then gives tips with whichever will give the maximum tips (number, black, white)
        # bonus: ive added with class attribute self.known_play_hand is bot keeps track of the players hand as they see it, and tips about unknown value and colors and stops if it has given all the tips it can already give.
        tip = ""
        mostRepeated = getMostRepeated(self.play_hand, self.known_play_hand) # a function to get the most repeated number on cards
        blackList = []
        whiteList = []
        rollDice = random.randint(1,6) # when the number of both black and white cards are the same (1 and 1 for when 2 cards remain) and the best tip is by giving a tip with colour,this rolldice adds a random chance on which colour is chosen for the tip (1,2,3 for black, 4,5,6 for white)

        for index in range (len(self.play_hand)) : # get number of colour of cards
          if self.known_play_hand[index][0] == "!" :
            if self.play_hand[index][0] == "b" :
              blackList.append([index, self.play_hand[index]])
            else :
              whiteList.append([index, self.play_hand[index]])
        # tip creating part
        if len(blackList) > 0 or len(whiteList) > 0 or len(mostRepeated) > 0 : # this determines if bot has new tips to give
          if len(blackList) > len(mostRepeated) and (len(blackList) > len(whiteList) or (len(blackList) ==  len(whiteList) and rollDice <= 3)) : # give tip about black cards
            for card in blackList :
              tip += str(card[0] + 1) + ","
              self.known_play_hand[card[0]][0] = "b"
            tip += "b"
          elif len(whiteList) > len(mostRepeated) and (len(whiteList) > len(blackList) or (len(whiteList) == len(blackList) and rollDice > 3)) : # give tip about white cards
            for card in whiteList :
              tip += str(card[0] + 1) + ","
              self.known_play_hand[card[0]][0] = "w"
            tip += "w"
          else : # give tip about the number of cards
            if len(mostRepeated) > 0 :
              for card in mostRepeated :
                tip += str(card[0] + 1) + ","
                self.known_play_hand[card[0]][1] = mostRepeated[0][1][1]
              tip += str(mostRepeated[0][1][1])
            else :
              index = random.randint(0, len(self.play_hand) - 1)
              tip += str(index + 1) + "," + str(self.play_hand[index][1])
              self.known_play_hand[index][1] = self.play_hand[index][1]
        else : # if bot has given all the tips about the players hand, it will say this instead.
          tip = "I have given all the possible tips."
        return tip
        
    def pick_stack(self): #YIGIT implement that same number as card number thing
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.

        # tries to find a card thats stackable
        # bonus: in the elif statement located at the very bottom of the function, bot checks if both stacks have the same number of cards, then if it finds a card with a number of 1 + number of cards in a stack, it stacks that card as its a guaranteed stack.
        found = False
        location = -1
        stackDict = {"b":0, "w":1, "!":2} # to use it in a inner if statement to determine if the color of the stack and the card are the same
        if len(self.hand) > 0 :
          for stackIndex in range(len(self.stack)) :
            for cardIndex in range(len(self.hand)) :
              if stackDict[self.hand[cardIndex][0]] == stackIndex : # determine if the cards color is the same as the stack
                if len(self.stack[stackIndex]) == 0 : # check if the stack is an empty stack
                  if self.hand[cardIndex][1] == 1 : # if the stack is empty, and a same coloured 1 card has been found, directly stack it to the empty stack
                    location = cardIndex + 1
                    print("found, stacking 1 to empty stack")
                    found = True
                    break
                elif self.hand[cardIndex][1] == self.stack[stackIndex][-1][1] + 1 : # if stacks are not empty, and if a card with one higher number than the last card in the stack, stack that card
                  location = cardIndex + 1
                  print("found, stacking the next one")
                  found = True
                  break
              elif location == -1 and len(stack[0]) == len(stack[1]) : # if both stacks have equal number of cards
                if self.hand[cardIndex][1] == len(stack[0]) + 1 : # and if we found a card which has a number of 1 + size of stack, consider appending it because its a guaranteed stack.(for instance, both stacks have 1 cards and we found a number 2 card, this will definetly stack.)
                  location = cardIndex + 1
                  found = True
                  break
                  

            if found :
              break
        return location
    

    def pick_discard(self): 
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.

        # it checks if one of the cards are already in a stack, and if so, discards it, other than that it tries to find the card with the minimum information and discard that
        # bonus: bot avoids discarding a 4 card, since they are rare.
        card2discard = 0
        determined = False # we will use this in the if statement at the bottom, to check if a card to discard is determined
        if len(self.hand) > 0 : # if bot has cards, it wouldve been impossible to discard from an empty hand
          for index in range(len(self.hand)) :
            if self.hand[index] in self.stack[0] or self.hand[index] in self.stack[1] :  # if a card thats already in a stack is found, stop and discard it immediately
              card2discard = index
              break
            elif self.hand[index] == ["!", -1] and self.hand[card2discard] != ["!", -1] : # if a completely unknown card is found, directly consider discarding it
              card2discard = index
              determined = True # bot has determined on a card to discard at least once
            elif (not self.hand[index][0].isalpha() or self.hand[index][1] not in [1,2,3,4]) and self.hand[card2discard] != ["!", -1] : # if a card with ! or -1 as values is found, consider discarding it if the current card to discard is not completely unknown
              if not determined or self.hand[index][1] != 4 : # since cards numbered 4 are very rare, bot will try to avoid discarding it
                card2discard = index
                determined = True
        print("ive found the discard location as " + str(card2discard))
        return card2discard + 1
    
    def update_known_play_hand(self, num) : # this is a function ive come up with, it will update the player hand as we know it, like how update_hand class function works.
      self.known_play_hand.pop(num - 1)
      if len(self.count_deck) > 3 : # 3 because these 3 can be on the bots hand
        self.known_play_hand.append(["!", -1])



def shuffle(deck):
  # input: deck to be shuffled
  # output: none
  # shuffle the deck
  # you are free to choose the algorithm you want
  # explain your shuffle algorithm in a comment

  # first i copy the original deck to a temporary deck, then clear the original deck, then append each card randomly from the temporary deck to the original deck, therefore ending up with a shuffled deck.
  tempDeck = list(deck)
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
    if len(deck) > 0 : # append a new card if there are cards in the deck
      hand.append(deck.pop(0))
    return removedCard

def try_stack(card,stack,trash,lives):
    # input: the card to be stacked, current stack, current trash, number of lives
    # output: updated number of lives
    # This function tries to place the card in the stack. If successful, the card is appropriately
    # added to the stack and the updated stack is printed. Otherwise, the card is appended to the
    # trash, the trash is sorted for better viewing and number of lives is decreased by 1. A warning
    # and the current number of lives are printed.

    #
    if card[0] == "b" : # index determines which stack (black or white) to stack on depending on the card color.
      index = 0
    else :
      index = 1
    if len(stack[index]) == 0 : # if a stack is empty, and the card number is 1, directly stack it
      if card[1] == 1 :
        stack[index].append(card)
        print("The current stack is: " + str(stack))
      else : # if the player is trying to stack a card with a different number than 1 to an empty stack, fail stacking, trash that card and decrease lives
        trash.append(card)
        trash.sort()
        lives -= 1
        print("Stacking unsuccessful. Remaining lives: " + str(lives))
    elif stack[index][-1][1] + 1 == card[1] : # if the last cards number plus one is the cards number we are trying to stack, directly stack it
      stack[index].append(card)
      print("The current stack is: " + str(stack))
    else : # if that fails, fail stacking process, trash that card and decrease lives
      trash.append(card)
      trash.sort()
      lives -= 1
      print("Stacking unsuccessful. Remaining lives: " + str(lives))
      print("The current trash is: " + str(trash))
    return lives

def discard(card,trash,tips):
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.

    # this function runs when bot or player intentionally wants to discard a card, to earn tips for instance.
    trash.append(card)
    trash.sort()
    tips += 1
    print("The trash is: " + str(trash))
    print("Remaining tips:" + str(tips))
    return tips

def getMostRepeated(sampleList, knownList) : # this is a function ive added, it helps me to get the most repeated number on a card so the bot can use this information on tip giving, sampleList is used as play_hand and knownList is used as known_play_hand in the code.
  frequency = {}
  for index in range(len(sampleList)) : #get frequency of numbers
    if knownList[index][1] == -1 : # this is a bonus, this checks if that cards number was given in a tip before
      if sampleList[index][1] not in frequency.keys() :
        frequency[sampleList[index][1]] = 1
      else :
        frequency[sampleList[index][1]] += 1
  mostRepeated = []
  if len(frequency.values()) > 0 :
    maxValue = max(frequency.values()) #get the highest frequency
    if maxValue > 1 : # if at least one card number repeats more than once
      for index in range(len(sampleList)) :
        if sampleList[index][1] in frequency.keys() and knownList[index][1] == -1 :
          if frequency[sampleList[index][1]] == maxValue :
            mostRepeated.append([index, sampleList[index]])
    else : #if no numbers repeat (all numbers are different), just select one of the unknown ones randomly
      index = -1 # placeholder index value
      firstRun = True # guarantees that while loop will run at least once
      while knownList[index][1] != -1 or firstRun :
        index = random.randint(0,len(sampleList) - 1) 
        firstRun = False
        print("are ya winnin son")
      mostRepeated.append([index, sampleList[index]])
  return mostRepeated

print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 4
shuffle(deck)
# First hands are dealt.
comp_hand = [deck[0], deck[1], deck[2]]  # i gave the first 3 cards to the ai. (# TODO: obtain cards (3 cards) from deck)
play_hand = [deck[3], deck[4], deck[5]] # i gave the next three to the player. (# TODO: obtain cards (3 cards) from deck)
del deck[0:6]
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
play_hand_change = False # i will use this to know if the players cards have changed or not since the last tip bot gave.
BotTip = "" # a placeholder for the tip that bot gives since i check it down there without recieving it first.
while True:
    print("debug: player has " +str(bot.play_hand) + " but you think that you have " + str(bot.known_play_hand))
    print("debug: bot has " + str(comp_hand) + " but it thinks that it has " + str(bot.hand))
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
                tip = str(input("Write the tip.")).split(",")
                while len(tip) < 2 or len(tip) > 4 or not tip[-1].isalnum() :
                  tip = str(input("Write the tip properly again.")).split(",")
                tips -= 1
                bot.get_tip(tip)
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            turn = 1        # Switch turns.
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
            if len(bot.play_hand) > 0 :
              num = int(input("Write the number of the card you would like to try stacking: "))
              stackCard = update_hand(bot.play_hand, deck, num)
              play_hand_change = True # since we updated players hand, it has changed.
              bot.update_known_play_hand(num) # update players known hand
              if len(bot.play_hand) == 3 :
                bot.update_count_deck(bot.play_hand[-1]) # if player has 3 cards, it means that there were enough cards to append a new one to player. so remove that appended card from the count deck.
              if len(bot.count_deck) == 3 : # if there are only 3 cards left in the count deck, this means that these 3 have to be the cards at bots hand, which means that bot knows its cards completely now. 
                bot.hand = comp_hand
                print("now i know all my cards")
              lives = try_stack(stackCard, stack, trash, lives)
            else :
              print("You have no cards to stack!")

        elif inp == "d":
            turn = 1        # Switch turns.
            # Take the location of the card to be discarded from the player,
            # update hands and bot's count_deck and discard the selected card.
            if len(bot.play_hand) > 0 :
              num = int(input("Write the number of the card you would like to discard: "))
              discardCard = update_hand(bot.play_hand, deck, num)
              play_hand_change = True  # players hand has changed
              bot.update_known_play_hand(num)
              if len(bot.play_hand) == 3 : # if player has 3 cards, that means they have appended a new card. remove the appended card from count deck.
                bot.update_count_deck(bot.play_hand[-1])
              if len(bot.count_deck) == 3 :
                bot.hand = comp_hand
                print("now i know all my cards")
              tips = discard(discardCard,trash,tips)
            else :
              print("You have no cards to discard!")

        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.

        if tips > 1 and len(bot.play_hand) > 0 and (BotTip != "I have given all the possible tips." or play_hand_change) : 
            # Take a tip from the bot. Update the number of tips. Print both
            # the given tip by the bot and the updated number of tips.

            # bonus: like i said in the tip giving part, a smarter rule set ive implemented to the tipping algorithm is the bot stops giving tips when there are no tips to give anymore, it tries to stack or discard instead. it also checks if the player hand has changed, and if so gives new tips after all tips were given to the previous player cards.
            # bonus: if there is only 3 cards in the count deck and since that means these 3 cards are at bots hand, bot will know the cards at its hand.
            BotTip = bot.give_tip()
            play_hand_change = False # since bot looked at the players hand and gave tips accordingly, this will stay false until players hand changes, so bot can come up with new tips.
            print(BotTip)
            if BotTip != "I have given all the possible tips." : # if a proper tip was given, decrease tips by one.
              tips -= 1
            else :
              print("No tips were deducted.") # this is more optional. it lets the player know that they currently know all of their cards, and gives them a turn again to think accordingly, without deducting tips since bot hasnt given a tip technically.
            print("Remaining tips: " + str(tips))
        else:
            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck
            # and discard the selected card.

            # if bot is able to stack, it will try to stack. else, it will pick a card to discard.
            location = bot.pick_stack()
            print("i found the stack location as " + str(location))
            if location != -1 : # if a card to stack was found
              botStackCard = update_hand(comp_hand, deck, location)
              print("im going to stack " + str(botStackCard))
              bot.update_hand(location)
              bot.update_count_deck(botStackCard)
              if len(bot.count_deck) == 3 :
                bot.hand = comp_hand
                print("now i know all my cards")
              lives = try_stack(botStackCard, stack, trash, lives)
            else :
              discardLocation = bot.pick_discard()
              botDiscardCard = update_hand(comp_hand, deck, discardLocation)
              bot.update_hand(discardLocation)
              bot.update_count_deck(botDiscardCard)
              if len(bot.count_deck) == 3 :
                bot.hand = comp_hand
                print("now i know all my cards")
              tips = discard(botDiscardCard, trash, tips)
              
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
