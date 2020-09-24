import pandas as pd
import site
import sys

site.addsitedir('.')

from alternate_energy import WindEnergy

def main():
    data = pd.read_csv('assignments/homework3/2006_tx.csv', header=0).values

    wind = WindEnergy(data[:, 0], data[:, 1])
    # Part 1: Plot data and calculate average wind speed
    print(" ".join([str(wind.average_speed()), "m/s"]))
    # TODO: Plot data
    wind.plot_speed()

    # Part 2: Calculate and plot pdf (probability vs wind speed)
    binned_data = wind.bin_data(data, num_bins=32)
    wind.plot_pdf(binned_data)

    # Part 3: Evaluate average power density (assume ro = 1.225 kg/m^3)
    print(" ".join([str(wind.average_speed_cubed()), "m/s"]))
    print(" ".join([str(wind.average_power_density()), "W/m^2"]))
    

if __name__ == "__main__":
    main()