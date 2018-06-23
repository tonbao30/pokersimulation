from deck import Deck
import pandas as pd
from time import clock
import matplotlib.pyplot as plt
import pylab
def change_in_chance():
    timing = []
    suit_return=[]
    rf_prob = []
    for suit in range(1,11):
        start_time = clock()
        s= Deck (2,14,suit)
        rf_prob.append(s.check_royalf(60000))
        end_time =clock ()
        timing.append(end_time-start_time)
        suit_return.append(suit)
    total_trial = len(s.sampledeck1)

    data = {'number of suits':suit_return ,\
            'avg_royal flush_prob':rf_prob,\
            'total_trial':[total_trial]*10}

    df = pd.DataFrame(data, columns=['number of suits','avg_royal flush_prob','total_trial'])
    df.to_csv('change in chance record.csv', sep=',', encoding='utf-8')
    print(df)
    plt.scatter(suit_return,timing,alpha=0.5)
    plt.ylabel('timing')
    plt.xlabel('number of suits')
    plt.title('Task 1.3 report')
    pylab.savefig('task 1.3.png')
    return plt.show()
def main():
    try:
        change_in_chance()
    except:
        print('error')
if __name__ == "__main__":
    main()