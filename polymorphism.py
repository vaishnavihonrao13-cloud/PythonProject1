class duck:
    def sound(self):
        return "quack"
class anotherbird:
    def sound(self):
        return"i'm simalar to duck"
def makesound(duck):
    print(duck.sound())
duck=duck()
anotherbird=anotherbird()
makesound(duck)
makesound(anotherbird)
