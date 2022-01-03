import sys
from PIL import Image

from Card import Card

class Gameboard:
    #basic player info: who the players are, the scale balance and who's turn it is
    player=["test", "bot"]
    scale=0
    playerTurn=0

    #places where cards are stored: the board, both player's hands and decks (which will be made as a temporary copy of the player's deck at the start of the match
    board=[["empty","empty","empty","empty","empty"],["empty","empty","empty","empty","empty"]]
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

    def testPrintCards(self):
        return self.printCards([Card(image="Leshy/Ant.png"),Card(image="Leshy/Amoeba.png",effects=["Sigils/Ability_AttackConduit.png"])])
