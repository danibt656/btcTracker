import requests
import time
import matplotlib.pyplot as plt
import numpy as np

MAX_RANGE = 100
DARK_BG = '#161616'
LINE = '#F19D62'
LABELS = '#ECDBBA'

def track():
    times = []
    values = []

    #plt.plot(times, values)
    plt.figure(facecolor=DARK_BG)

    ax = plt.axes()
    ax.set_facecolor(DARK_BG)
    ax.spines['bottom'].set_color(LABELS)
    ax.spines['left'].set_color(LABELS)
    ax.spines['right'].set_color(LABELS)
    ax.spines['top'].set_color(LABELS)
    ax.xaxis.label.set_color(LABELS)
    ax.yaxis.label.set_color(LABELS)
    ax.tick_params(colors=LABELS, which='both')
    ax.set_title('BTC value', color=LABELS)

    plt.xlabel('time [epoch]')
    plt.ylabel('value [$USD]')
    #plt.title('BTC value')

    for i in range(MAX_RANGE):
        url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
        response = requests.get(url).json()
        value = response["USD"]
        timeNow = time.time()

        print(f"[{i}]: {value}, {timeNow}")

        times.append(timeNow)
        values.append(value)

        #plt.scatter(timeNow, value)
        plt.plot(times, values, color=LINE)
        plt.pause(0.05)

    plt.show()



def main2():
    times, values = track()

    plt.plot(times, values)
    plt.xlabel('time [epoch]')
    plt.ylabel('value [$USD]')
    plt.title('BTC value')

    plt.show()

def main():
    for i in range(10):
        y = np.random.random()
        plt.scatter(i, y)
        plt.pause(0.05)

    plt.show()



if __name__ == '__main__':
    track()
