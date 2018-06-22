class Card:

    def __init__(self,faceValue,suitType):
        self.face = faceValue
        self.suit = suitType

    def getFace(self):
        return self.face

    def getSuit(self):
        return self.suit

    def __str__(self):
        return str(self.getFace()) + ":" + str(self.getSuit())
def main():


    a=Card(1,2)
    print(a)
if __name__ == "__main__":
    main()