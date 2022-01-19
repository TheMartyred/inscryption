from Card import Card

class Player:
    name = ""
    ID = ""
    deck = []
    items = []
    lives = 1
    totemBases=[]
    totemHeads=[]
    character="player"

    def __init__(self, ID, name=None, deck=[], items=[], lives=2, totemBases=[], totemHeads=[], character="player"):
        self.ID=ID
        if name == None:
            self.name=ID
        else:
            self.name=name
        self.deck=deck
        self.itens=items
        self.lives=lives
        self.totemBases=totemBases
        self.totemHeads=totemHeads
        self.character=character
