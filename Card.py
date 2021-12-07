class Card:
    name="glitch"
    atk=0
    hp=1
    image="Leshy/Glitched_Card.gif"
    effects=[]
    cost=0
    currency="blood"
    health=1

    def __init__(self, name="glitch", atk=0, hp=1, image="Leshy/Glitched_Card.gif", effects=[], cost=0, currency="blood"):
        self.atk=atk
        self.hp=hp
        self.name=name
        self.image=image
        self.effects=effects
        self.cost=cost
        self.currency=currency
        self.health=hp

    def __str__(self):
        retun=""+self.name+"\n"+str(self.atk)+" attack power, "+str(self.health)+"/"+str(self.hp)+" health points\n"
        for x in self.effects:
            retun+=""+x+", "
        retun+="\ncosts: "+str(self.cost)+" "+self.currency
        return retun

    def takeDamage(self, damage):
        self.health-=damage
