from deck import Deck

def main():
    try:
        check_deck=Deck(1,13,4)
        check_deck.check_fairness()
    except:
        print('error!!!')

if __name__ == "__main__":
    main()


