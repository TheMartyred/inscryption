import sys
from PIL import Image

class Card:
    #pseudo permanent stats: These remain across multiple matches but can be altered between
    name="glitch"
    atk=0
    hp=1
    image="Leshy/Glitched_Card.gif"
    effects=[]
    cost=0
    currency="blood"
    clan="none"

    #temporary stats: These respresent the card's current stats and reset when a match is over
    health=hp
    power=atk
    tempEffects=[]

    def __init__(self, name="glitch", atk=0, hp=1, image="Leshy/Glitched_Card.gif", effects=[], cost=0, currency="blood"):
        """initialization method: takes all stats as optional arguments, defaults to a test 'glitched' card"""
        self.atk=atk
        self.hp=hp
        self.name=name
        self.image=image
        self.effects=effects
        self.cost=cost
        self.currency=currency
        
        self.health=hp
        self.power=atk

    def __str__(self):
        """to string return method: displays all the cards stats in text form"""
        retun=""+self.name+"\n"+str(self.atk)+" attack power, "+str(self.health)+"/"+str(self.hp)+" health points\n"
        for x in self.effects:
            retun+=""+x+", "
        retun+="\ncosts: "+str(self.cost)+" "+self.currency+"\nClan: "+self.clan
        return retun

    def takeDamage(self, damage):
        """used to decrease a card's dealth when it takes combat damage"""
        self.health-=damage
        
    def reset(self):
        """Called when a card is destroyed or a match ends to reset a cards current stats and effects to its permanent ones"""
        self.health=self.hp
        self.power=self.atk
        self.tempEffects=[]

    def buffCard(self, stat, change):
        """called when a card is altered permanently by adding to its stats or effects"""
        if stat == "hp":
            self.hp+=change
        if stat == "atk":
            self.atk+=change
        if stat == "effect":
            self.effects.append(change)
        self.reset()
