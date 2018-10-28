#!/usr/bin/env python


import jhtalib as jhta
import matplotlib.pyplot as plt


def main():
    df = jhta.CSV2DF('data.csv')
    x = df['datetime']

    plt.figure(1)

    plt.subplot(211)
    plt.title('Time / Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.plot(x, df['Close'], color='blue')
    plt.plot(x, jhta.SMA(df, 200), color='red')
    plt.legend(['Close', 'SMA 200'], loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()

