import numpy as np
import matplotlib.pyplot as plt

class Wind:
    def __init__(self, dates, speeds):
        self.dates = dates
        self.speeds = speeds

    def plot_speed():
        fig = plt.figure()
        fig, ax = plt.subplots()
        ax.plot(self.dates, self.speeds)
        ax.set_ylabel('Speed [m/s]')
        ax.set_xlabel('Date & Time')

    def average_speed(self):
        count = self.speeds.size
        probability = 1/count
        return np.sum(self.speeds * probability)

    def speed_cubed_average(self):
        pass

