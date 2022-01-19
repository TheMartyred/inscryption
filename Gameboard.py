import sys
from PIL import Image

from Card import Card

class Gameboard:
    #basic player info: who the players are, the scale balance and who's turn it is
    player=["test", "bot"]
    scale=0
    playerTurn=0

    #places where cards are stored: the board, both player's hands and decks (which will be made as a temporary copy of the player's deck at the start of the match
    board=[[Card(),Card(),Card(),Card(),Card()],[Card(),Card(),Card(),Card(),Card()]]
    hand=[[],[]]
    deck=[[],[]]

    #information regarding the various currencies in the game. The turn number, which max batteries is based on, current usable batteries and each player's bone reservoir
    #mox are handled by the game board and blood is handled on a basis of need
    turn=0
    batteries=turn
    bloodNeed=0
    bones=[0,0]

    def __init__(self, player0="test", player1="bot", deck0=[], deck1=[]):
        """initialization method: takes players and their decks. default values are for testing"""
        self.player[0]=player0
        self.player[1]=player1
        self.deck[0]=deck0
        self.deck[1]=deck1

    def printCards(self, cards):
        """returns a composite image of all the cards in the specified array"""
        images = [x.printCard() for x in cards]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]
        return new_im

    def turn(self):
        """colculates the result of a turn with current boardstate"""
        #set opposing player to whatever playerTurn isn't mathematically
        opposingPlayer=(self.playerTurn+1)%2
        #for each space on the game board
        #for x in len(self.board[self.playerTurn]):
        for x in range(len(self.board[1])):
            #make a copy of the card
            activeCard=self.board[self.playerTurn][x]
            #if it's an empty space, do nothing
            if "empty space" in activeCard.special:
                print("turn processed empty space")
            else:
                #otherwise, determine which card is across from it
                opposingCard=self.board[opposingPlayer][x]
                #if opposing space is empty, deal direct damage
                if "empty space" in opposingCard.special:
                    self.scale+=(self.playerTurn*2-1)*activeCard.atk
                else:
                    #otherwise, deal damage to the card
                    opposingCard.takeDamage(activeCard.atk)
                    #kill it if its hp is 0
                    if opposingCard.health<=0:
                        self.board[opposingPlayer][x]=Card()
                    else:
                        #otherwise, save that card back to the spot on the board
                        self.board[opposingPlayer][x]=opposingCard
        self.playerTurn=opposingPlayer
        #set the player turn to the oher player ^^^
        #print scale state
        print(self.scale)

    def testPrintCards(self):
        return self.printCards([Card(image="Leshy/Ant.png"),Card(image="Leshy/Amoeba.png",effects=["Sigils/Ability_AttackConduit.png"])])
