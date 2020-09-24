import numpy as np
import pandas as pd
import matplotlib.dates as dates
import matplotlib.pyplot as plt

class WindEnergy:
    def __init__(self, dates, speeds):
        self.dates = dates
        self.speeds = speeds

    def plot_speed(self):
        """Create a plot of the wind speed data for the WindEnergy object"""
        converted_dates = dates.datestr2num(self.dates)
        fig, ax = plt.subplots()
        ax.xaxis.set_major_formatter(dates.DateFormatter('%m/%d/%Y %H:%M'))
        ax.xaxis.set_major_locator(dates.DayLocator(interval=25))
        ax.plot(converted_dates, self.speeds)
        ax.set_ylabel('Speed [m/s]')
        fig.autofmt_xdate()
        plt.show()

    def average_speed(self) -> int:
        """Calculate the average wind speed over a numpy array"""
        count = self.speeds.size
        probability = 1/count
        return np.sum(self.speeds * probability)

    def average_speed_cubed(self) -> int:
        """Calculate the wind speed cubed average of the wind speed data"""
        count = self.speeds.size
        probability = 1/count
        return np.sum(self.speeds**3 * probability)

    def average_power_density(self, ro: int = 1.225, speed_cubed: int = None):
        _speed_cubed = speed_cubed
        if speed_cubed is None:
            _speed_cubed = self.average_speed_cubed()
        
        return 0.5 * ro * _speed_cubed

    def bin_data(self, data_frame, num_bins: int = 24):
        """Create bins of data for wind probability analysis"""
        binned_data = pd.cut(data_frame[:, 1], num_bins)
        
        binned_speeds = binned_data.categories.mid.values
        binned_speeds_counts = binned_data.value_counts().values
        probabilities = binned_speeds_counts/data_frame[:, 1].size

        return {'binned_speeds': binned_speeds, 'counts': binned_speeds_counts, 'probabilities': probabilities}

    def plot_pdf(self, data):
        """Input data from bin_data and create a probability distribution plot"""
        fig, ax = plt.subplots()
        ax.plot(data['binned_speeds'], data['probabilities'])
        ax.set_ylabel('Probability')
        ax.set_xlabel('Wind Speed [m/s]')
        plt.show()

