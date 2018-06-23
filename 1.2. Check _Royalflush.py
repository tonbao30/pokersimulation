from deck import Deck
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab
def check_royal_flush():
    totaltrials =[]
    rf_prob = []
    for n in range (10):
        a = Deck(2, 14, 4)
        totaltrials.append(n+1)
        rf_prob.append(a.check_royalf(60000))
    total_trial = len(a.sampledeck1)
# export data
    data = {'trial_set_no.': totaltrials,
            'avg_royal_flush_prob': rf_prob,
            'total_trial': [total_trial] * 10
            }
    df = pd.DataFrame(data, columns=['trial_set_no.', 'avg_royal_flush_prob', 'total_trial'])
    df.to_csv('royal flush trial record.csv',sep=',',encoding='utf-8')
    data2 = {'number of draws': [total_trial *10],
            'royal_flush_prob': [sum(rf_prob)/total_trial*10],
           }
    df2 = pd.DataFrame(data2, columns=['number of draws', 'royal_flush_prob'])
    print(df)
    print(df2)
    # plot
    y_mean = [np.mean(rf_prob)] * 10
    fig, ax = plt.subplots()
    ax.bar(totaltrials, rf_prob, align='center', alpha=0.5)
    ax.plot(totaltrials, y_mean, label='Mean', linestyle='--')
    plt.xlabel('trial times')
    plt.ylabel('probability')
    plt.title('Task 1.2 royal flush report')
    plt.show()
    pylab.savefig('task 1.2.png')


def main():

       check_royal_flush()

if __name__ == "__main__":
    main()
