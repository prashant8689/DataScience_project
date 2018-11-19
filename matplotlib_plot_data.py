# import packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import collections


# plt(x, y)         # plot x and y using default line style and color
# plt(x, y, 'bo')   # plot x and y using blue circle markers
# plt(y)            # plot y using x as index array 0..N-1
# plt(y, 'r+')      # ditto, but with red plusses
#
# https://matplotlib.org/2.2.3/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
def plot_data(header, data):
    # Plot the data
    filter_data = data["India" == data[:, 2]]  # Filtering data for country == "India"

    plt.title('sales-rank graph!')
    plt.xlabel('rank')  # Labeling x axis with name "rank"
    plt.ylabel('sales')  # Labeling y axis with name "sales"
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 4]))  # Plotting graph for column 0 as x axis and column 4 as y axis.
    plt.show()  # Showing plotted graph.

    plt.title('Profit-rank graph!')
    plt.xlabel('rank')  # Labeling x axis with name "rank"
    plt.ylabel('profit')  # Labeling y axis with name "profit"
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 5]))  # Plotting graph for column 0 as x axis and column 5 as y axis.
    plt.show()  # Showing plotted graph.

    plt.title('asset-rank graph!')
    plt.xlabel('rank')  # Labeling x axis with name "rank"
    plt.ylabel('asset')  # Labeling y axis with name "sasset"
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 6]))  # Plotting graph for column 0 as x axis and column 6 as y axis.
    plt.show()  # Showing plotted graph.

    plt.title('marketValue-rank graph!')
    plt.xlabel('rank')  # Labeling x axis with name "rank"
    plt.ylabel('marketValue')  # Labeling y axis with name "MarketValue"
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 7]))  # Plotting graph for column 0 as x axis and column 7 as y axis.
    plt.show()  # Showing plotted graph.

    # https: // docs.python.org / 2 / library / collections.html  # collections.Counter
    counter = collections.Counter(data[:, 3])
    print dict(counter)
    print type(dict(counter))
    plt.title('catagory-count graph!')
    plt.xlabel('No. of companies')  # Labeling x axis with name "company count"
    plt.ylabel('Catagories')  # Labeling y axis with name "Catagory"
    # plt.bar(counter.keys(), counter.values())  # Plotting bar graph for column 0 as x axis and column 5 as y axis.
    plt.scatter(counter.values(), counter.keys())
    plt.show()  # Showing plotted graph.


# http://docs.astropy.org/en/stable/visualization/histogram.html
# https://matplotlib.org/2.2.3/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
# https://matplotlib.org/2.2.3/gallery/statistics/histogram_features.html
def plot_histogram(data):
    filter_data = data
    # filter_data = data["India" == data[:, 2]]  # filter the data for country == "India"
    # Collecting the profit column data.
    # Do do so, first need to get the transpose of matrix.
    # since all the data will be in string format so applying float to all values of transposed data using map function.
    # profit_data = map(float, filter_data[:, 5])  # Collect the profit data
    profit_data = map(lambda x: float(0) if x == "NA" else float(x), filter_data[:, 5])
    print profit_data
    # setting the ranges and no. of intervals
    rnge = (-20, 20)
    bins = 70

    # plotting a histogram
    plt.hist(profit_data, bins, rnge, color='green', histtype='bar', rwidth=.7)
    plt.xlabel('profit')
    plt.ylabel('No of companies')
    plt.title('Histogram of profit against company count')
    # plt.hist(profit_data)
    # plt.axis([0, 2000, 0, 200])
    # plt.grid(True)
    plt.show()
