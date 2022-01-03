import sys
from PIL import Image

class Card:
    #pseudo permanent stats: These remain across multiple matches but can be altered between
    name="glitch"
    atk=0
    hp=1
    image="Leshy/Glitched_Card.gif"
    effects=[] #will need to be named after the file names of the sigils for card print method to work
    cost=0
    currency="blood"
    clan="none"
    bleeds=True

    #temporary stats: These respresent the card's current stats and reset when a match is over
    health=hp
    power=atk
    tempEffects=[]

    def __init__(self, name="glitch", atk=0, hp=1, image="Leshy/Glitched_Card.gif", effects=[], cost=0, currency="blood", bleeds=True):
        """initialization method: takes all stats as optional arguments, defaults to a test 'glitched' card"""
        self.atk=atk
        self.hp=hp
        self.name=name
        self.image=image
        self.effects=effects
        self.cost=cost
        self.currency=currency
        self.bleeds=bleeds
        
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

    def printCard(self):
        """returns a composite image of the card"""
        #retrieve card image
        cardImage = [Image.open(self.image)]
        #get size of card image
        widths, heights = zip(*(i.size for i in cardImage))
        total_width = sum(widths)
        max_height = max(heights)
        print(str(total_width)+" by "+str(max_height))
        #create matching new image
        new_im = Image.new('RGBA', (total_width, max_height))
        new_im.paste(cardImage[0], (0,0))
        #add sigils
        print(self.effects)
        images = [Image.open(x) for x in self.effects]
        y_offset = 0
        for im in images:
            new_im.paste(im, (0,y_offset), im.convert("RGBA"))
            y_offset += im.size[0]
        return new_im
