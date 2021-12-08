from Card import Card

class Player:
    name = ""
    deck = []
    items = []
    lives = 1
    totemBases=[]
    totemHeads=[]
    character="player"

    def __init__(self, name, deck=[]):
