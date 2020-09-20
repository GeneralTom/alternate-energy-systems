import pandas as pd
import matplotlib.pyplot as plt
import site
import sys

site.addsitedir('.')

from alternate_energy import Wind

def main():
    data = pd.read_csv('assignments/homework3/2006_tx.csv', header=0).values

    fig = plt.figure()
    fig, ax = plt.subplots()
    ax.plot(data[:, 0], data[:, 1])

    # wind = Wind()

if __name__ == "__main__":
    main()