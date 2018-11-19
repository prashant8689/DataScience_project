# import packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# plt(x, y)         # plot x and y using default line style and color
# plt(x, y, 'bo')   # plot x and y using blue circle markers
# plt(y)            # plot y using x as index array 0..N-1
# plt(y, 'r+')      # ditto, but with red plusses
#
# https://matplotlib.org/2.2.3/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
def plot_data(header, data):
    # Plot the data
    filter_data = data["India" == data[:, 2]]  # Filtering data for country == "India"
    plt.xlabel('rank')  # Labeling x axis with name "rank"
    plt.ylabel('profit')  # Labeling y axis with name "profit"
    plt.plot(filter_data[:, 0], filter_data[:, 5])  # Plotting graph for column 0 as x axis and column 5 as y axis.
    plt.show()  # Showing plotted graph.


# http://docs.astropy.org/en/stable/visualization/histogram.html
# https://matplotlib.org/2.2.3/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
# https://matplotlib.org/2.2.3/gallery/statistics/histogram_features.html
def plot_hostogram(data):
    filter_data = data["India" == data[:, 2]]  # filter the data for country == "India"
    # Collecting the profit column data.
    # Do do so, first need to get the transpose of matrix.
    # since all the data will be in string format so applying float to all values of transposed data using map function.
    profit_data = map(float, np.transpose(filter_data)[6])  # Collect the profit data
    mu = np.mean(profit_data)  # Calculating the mean of distribution
    sigma = np.std(profit_data)  # Calculating the standard deviation of distribution
    
    n, bins, patches = plt.hist(profit_data, 50, density=1, facecolor='green', alpha=0.75)
    plt.plot(bins, 'r--', linewidth=1)
    plt.xlabel('rank')
    plt.ylabel('profit')
    plt.title('Histogram of profit against company rank: mu=%s, sigma=%s'% (mu, sigma))
    plt.axis([0, 2000, 0, 50])
    plt.grid(True)

    # Tweak spacing to prevent clipping of ylabel
    # fig.tight_layout()
    plt.show()
