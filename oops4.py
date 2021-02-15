import sys
from termcolor import colored, cprint
from random import shuffle
class Card:
    suits = ("spades","hearts","diamonds","clubs")
    values = (None, None,"2", "3","4","5","6","7","8","9","10","Jack","Queen","King","Ace")

    #The items at the first two indexs of the values tuple are None, so that the strings in the tuple match up with the index they represent-so the string "2" in the values tuple is at index 2.

    def __init__(self,v,s):
        self.value = v
        self.suit = s

#The suits are arranged in order of strength in the suits tuple--with the strongest suit last, and thus assigned the highest index, and the least powerful suit assigned the lowest index.

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
#the two magic methods alllow you to compare two card objects in an expression using greater than and less than operators.
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
        +self.suits[self.suit]
        return v
#card = Card(3, 1)
#print(card)

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
# first loop is from 2 to 15 because the first value for a card is 2 and the last value for a card is 14(the ace). This process creates 52 cards. After this the shuffle method from the random module randomly rearranges the item in the cards list.
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
#rm method removes and returns a card from the cards list or returns none if it is empty. you can use the Deck class to create new deck of cards and print each card on it.
#deck = Deck()
#for card in deck.cards:
    #print(card)
#need a class to represent player. to keep track of their cards and how many rounds they've won.
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

#the player class has 3 instance variables wins to keep track of how many rounds a player has won, card to represent the card a player is currently holding and name to keep track of a player's name.


#GAME
class Game:
    def __init__(self):
        name1 = input(" PLAYER 1 NAME: ")
        name2 = input(" PLAYER 2 NAME: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    #when you create the game object python calls __init__ method, and the input function collects names of the 2 players & stores them in a variable. now you create a new Deck object, store it in the instance variable deck.
    #and create 2 player objects using the names in name1 and name2.

    def wins(self, winner):
        w = "{} wins this round."
        w = w.format(winner)
        print(w)
#the method play_game starts the game. the loop will run till 2 or more cards are left in the deck. And as long as variable response does not equal q.  each time around the loop, you assign the variable response to the input of the user.
    def draw(self, p1n,p1c,p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n,p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        cprint("""






 __       _______ .___________.   .___________. __    __   _______    ____    __    ____  ___      .______         .______    _______   _______  __  .__   __.
|  |     |   ____||           |   |           ||  |  |  | |   ____|   \   \  /  \  /   / /   \     |   _  \        |   _  \  |   ____| /  _____||  | |  \ |  |
|  |     |  |__   `---|  |----`   `---|  |----`|  |__|  | |  |__       \   \/    \/   / /  ^  \    |  |_)  |       |  |_)  | |  |__   |  |  __  |  | |   \|  |
|  |     |   __|      |  |            |  |     |   __   | |   __|       \            / /  /_\  \   |      /        |   _  <  |   __|  |  | |_ | |  | |  . `  |
|  `----.|  |____     |  |            |  |     |  |  |  | |  |____       \    /\    / /  _____  \  |  |\  \----.   |  |_)  | |  |____ |  |__| | |  | |  |\   |
|_______||_______|    |__|            |__|     |__|  |__| |_______|       \__/  \__/ /__/     \__\ | _| `._____|   |______/  |_______| \______| |__| |__| \__|




                                                                                                                              """, 'green', attrs=['bold'], file=sys.stderr)

        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        cprint("""







────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████──██████████████──████████████████────██████████──██████████████──██████████████──██████──██████──██████████████──████████████████───
─██░░██──────────██░░██──██░░░░░░░░░░██──██░░░░░░░░░░░░██────██░░░░░░██──██░░░░░░░░░░██──██░░░░░░░░░░██──██░░██──██░░██──██░░░░░░░░░░██──██░░░░░░░░░░░░██───
─██░░██──────────██░░██──██░░██████░░██──██░░████████░░██────████░░████──██░░██████████──██░░██████░░██──██░░██──██░░██──██░░██████████──██░░████████░░██───
─██░░██──────────██░░██──██░░██──██░░██──██░░██────██░░██──────██░░██────██░░██──────────██░░██──██░░██──██░░██──██░░██──██░░██──────────██░░██────██░░██───
─██░░██──██████──██░░██──██░░██████░░██──██░░████████░░██──────██░░██────██░░██████████──██░░██──██░░██──██░░██──██░░██──██░░██████████──██░░████████░░██───
─██░░██──██░░██──██░░██──██░░░░░░░░░░██──██░░░░░░░░░░░░██──────██░░██────██░░░░░░░░░░██──██░░██──██░░██──██░░██──██░░██──██░░░░░░░░░░██──██░░░░░░░░░░░░██───
─██░░██──██░░██──██░░██──██░░██████░░██──██░░██████░░████──────██░░██────██████████░░██──██░░██──██░░██──██░░██──██░░██──██░░██████████──██░░██████░░████───
─██░░██████░░██████░░██──██░░██──██░░██──██░░██──██░░██────────██░░██────────────██░░██──██░░██──██░░██──██░░░░██░░░░██──██░░██──────────██░░██──██░░██─────
─██░░░░░░░░░░░░░░░░░░██──██░░██──██░░██──██░░██──██░░██████──████░░████──██████████░░██──██░░██████░░██──████░░░░░░████──██░░██████████──██░░██──██░░██████─
─██░░██████░░██████░░██──██░░██──██░░██──██░░██──██░░░░░░██──██░░░░░░██──██░░░░░░░░░░██──██░░░░░░░░░░██────████░░████────██░░░░░░░░░░██──██░░██──██░░░░░░██─
─██████──██████──██████──██████──██████──██████──██████████──██████████──██████████████──██████████████──────██████──────██████████████──██████──██████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────




                                                                      {}




                        ────────────────────────────────────────────────────────────────────────────
                        ─██████──────────██████──██████████──██████──────────██████──██████████████─
                        ─██░░██──────────██░░██──██░░░░░░██──██░░██████████──██░░██──██░░░░░░░░░░██─
                        ─██░░██──────────██░░██──████░░████──██░░░░░░░░░░██──██░░██──██░░██████████─
                        ─██░░██──────────██░░██────██░░██────██░░██████░░██──██░░██──██░░██─────────
                        ─██░░██──██████──██░░██────██░░██────██░░██──██░░██──██░░██──██░░██████████─
                        ─██░░██──██░░██──██░░██────██░░██────██░░██──██░░██──██░░██──██░░░░░░░░░░██─
                        ─██░░██──██░░██──██░░██────██░░██────██░░██──██░░██──██░░██──██████████░░██─
                        ─██░░██████░░██████░░██────██░░██────██░░██──██░░██████░░██──────────██░░██─
                        ─██░░░░░░░░░░░░░░░░░░██──████░░████──██░░██──██░░░░░░░░░░██──██████████░░██─
                        ─██░░██████░░██████░░██──██░░░░░░██──██░░██──██████████░░██──██░░░░░░░░░░██─
                        ─██████──██████──██████──██████████──██████──────────██████──██████████████─
                        ────────────────────────────────────────────────────────────────────────────







  """.format(win), 'red', attrs=['bold'], file=sys.stderr)
#2 cards are drawn each time through the loop. and play_game method assigns the first card p1 and the second card to p2. Then it prints name of each player and the card they drew. Compares 2 cards to see
#which card is greater and increments the wins instance variable for the player with the greater card and declares the message who won the most games.
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()
