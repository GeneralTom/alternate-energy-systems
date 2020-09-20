import pandas as pd
import site
import sys

site.addsitedir('.')

from alternate_energy import Wind

def main():
    data = pd.read_csv('assignments/homework3/2006_tx.csv', header=0).values

    wind = Wind(data[:, 0], data[:, 1])
    print(wind.average_speed())
    wind.plot_speed()

if __name__ == "__main__":
    main()