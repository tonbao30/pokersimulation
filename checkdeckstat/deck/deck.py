
from card import Card
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Deck:

    def __init__(self, valueStart, valueEnd, numSuits):
        self.pile = []
        self.size = 0
        self.sampledeck = []
        self.sampledeck1 = []
        self.hand_face = []
        self.hand_suit = []
        self.numsuit = numSuits

        values = []

        i = valueStart

        while i <= valueEnd:
            values.append(i)
            i += 1

        i = 0

        while i < numSuits:
            for value in values:
                newCard = Card(value,i)
                self.pile.append(newCard)
                self.size += 1
            i += 1

    def __str__(self):
        newString = ""

        for card in self.pile:
            newString += (str(card) + ',')

        newString = newString[:-1]

        return newString
    def __repr__(self):
        return 'Deck()'
    def __len__(self):
        return self.size

    #adds an item at location where
    def addCard(self, card, where):
        if where > -1 and where <= self.size:
            self.pile = self.pile[:where] + [card] + self.pile[where:]
            self.size += 1
        else:
            print("I can't add there.")

    #draw a card from the top of the deck
    def drawCard(self):
        item = self.pile.pop()
        self.size -= 1

        return item

    def placeCardTop(self, card):
        self.addCard(card, self.size)

    def placeCardBottom(self,card):
        self.addCard(card, 0)

    def shuffle(self,**kwargs):

        newPile = []

        if "seed" in kwargs:
            seed(kwargs["seed"])

        while len(self.pile) > 0:
            item = random.randint(0, len(self.pile)-1)

            newPile.append(self.pile[item])

            del(self.pile[item])

        self.pile = newPile

    # check deck fairness function
    def check_fairness(self):
        for i in range(1000):
            self.shuffle()
            self.placeCardBottom(self.drawCard())
            self.sampledeck.append(self.pile[0].face)
        sample = pd.Series(self.sampledeck)
        s = sample.value_counts(sort=True)
        df = pd.DataFrame({'Face_value': s.index, 'count': s.values})
        print(df)
        print(sample.describe()[['count','mean']])
        y_mean = [np.mean(s.values)/1000] * len(list(set(self.sampledeck)))
        fig, ax = plt.subplots()
        ax.bar(list(set(self.sampledeck)), s.values/1000, align='center', alpha=0.5)
        ax.plot(list(set(self.sampledeck)), y_mean, "--")
        plt.xlabel('face value')
        plt.title('Task 1.1 face probability report')
        plt.ylabel('face probability')
        fig.savefig("task1.1.png")
        plt.show()

    # check royal flush function
    def check_royalf(self,trials):
        try:
            for i in range (trials):
                for k in range (5):
                    self.shuffle()
                    self.placeCardBottom(self.drawCard())
                    self.hand_face.append(self.pile[0].face)
                    self.hand_suit.append(self.pile[0].suit)
                self.sampledeck1.append([sum(self.hand_face),len(set((self.hand_suit)))])
                self.hand_face = []
                self.hand_suit = []
            b = np.array(self.sampledeck1)
            df = pd.DataFrame(np.hstack([b, np.random.randn(len(self.sampledeck1), 1).round(2)]),
                              columns=['val_face', 'val_suit', 'occur'])
            df[['val_face', 'val_suit', 'occur']] = df[['val_face', 'val_suit', 'occur']].astype(float)
            df.groupby(['val_face', 'val_suit']).agg(['count'])
            pd.set_option('display.max_rows', 100000)
            new_df = df.groupby(['val_face', 'val_suit']).agg(['count'])
            new_df1 = df.groupby(['val_face', 'val_suit']).agg({'occur': 'sum'})
            new_df2 = new_df.groupby(level=0).apply(lambda x: 1 * x / float(len(self.sampledeck1)))
            rflushprob = new_df2.query('(val_face == 60)&(val_suit == 1)')

            # return the probability of the royal flush if it drawn successful
            return (rflushprob.iloc[0]['occur'].get_value('count'))/self.numsuit

        # return the probability of the royal flush if it drawn unsuccessful which is 0
        except IndexError:
            return 0

def main():
    new_deck = Deck(1, 3, 11)
    print(new_deck)
    testCard = Card(6,6)
    new_deck.placeCardTop(testCard)
    new_deck.placeCardBottom(testCard)
    print(new_deck)
    new_deck.shuffle()
    print(new_deck)

    print(new_deck.check_royalf(10))
    print(new_deck.check_fairness())
if __name__ == "__main__":
    main()