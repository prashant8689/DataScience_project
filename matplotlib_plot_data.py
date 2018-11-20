# import packages
import numpy as np
import matplotlib.pyplot as plt
import collections

np.set_printoptions(threshold=np.nan)

# plt(x, y)         # plot x and y using default line style and color
# plt(x, y, 'bo')   # plot x and y using blue circle markers
# plt(y)            # plot y using x as index array 0..N-1
# plt(y, 'r+')      # ditto, but with red plusses
#
# https://matplotlib.org/2.2.3/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
def plot_data(header, data):
    # Plot the data
	
	# Filtering data for country == "India"
    filter_data = data["India" == data[:, 2]]  

	# plot title with name "sales-rank graph"
    plt.title('sales-rank graph')
	
	# Labeling x axis with name "rank"
    plt.xlabel('rank')
	
	# Labeling y axis with name "sales"
    plt.ylabel('sales')
	
	# Plotting graph for column 0 as x axis and column 4 as y axis.
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 4]))
    # Showing plotted graph.
	plt.show()

	
	# plot title with name "Profit-rank graph"
    plt.title('Profit-rank graph')
	
	# Labeling x axis with name "rank"
    plt.xlabel('rank')  
	
	# Labeling y axis with name "profit"
    plt.ylabel('profit')  
	
	# Plotting graph for column 0 as x axis and column 5 as y axis.
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 5]))  
	
	# Showing plotted graph.
    plt.show()  

	
	# plot title with name "asset-rank graph"
    plt.title('asset-rank graph')
	
	# Labeling x axis with name "rank"
    plt.xlabel('rank')  
	
	# Labeling y axis with name "asset"
    plt.ylabel('asset')  
	
	# Plotting graph for column 0 as x axis and column 6 as y axis.
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 6]))  

	# Showing plotted graph.
    plt.show()  


	# plot title with name "marketValue-rank graph"
    plt.title('marketValue-rank graph')
	
	# Labeling x axis with name "rank"
    plt.xlabel('rank')  
	
	# Labeling y axis with name "MarketValue"
    plt.ylabel('marketValue')  
	
	# Plotting graph for column 0 as x axis and column 7 as y axis.
    plt.plot(filter_data[:, 0], map(float, filter_data[:, 7]))  
	
	# Showing plotted graph.
    plt.show()  

    # https: // docs.python.org / 2 / library / collections.html  # collections.Counter
    counter = collections.Counter(data[:, 3])
	
	# plot title with name "catagory-count graph"
    plt.title('catagory-count graph')
	
	# Labeling x axis with name "company count"
    plt.xlabel('No. of companies')  
	
	# Labeling y axis with name "Catagory"
    plt.ylabel('Catagories')  
	
	# Plotting bar graph for column 0 as x axis and column 5 as y axis.
    # plt.bar(counter.keys(), counter.values())  
    plt.scatter(counter.values(), counter.keys())
	
	# Showing plotted graph.
    plt.show()  


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

    # setting the ranges and no. of intervals
    rnge = (-20, 20)
    bins = 70

    # plotting a histogram
    plt.hist(profit_data, bins, rnge, color='green', histtype='bar', rwidth=.7)
	
	# Labeling x axis with name "profit"
    plt.xlabel('profit')
	
	# Labeling y axis with name "No of companies"
    plt.ylabel('No of companies')
	
	# plot title with name "Histogram of profit against company count"
    plt.title('Histogram of profit against company count')
	
	# Showing plotted graph.
    # plt.hist(profit_data)
    # plt.axis([0, 2000, 0, 200])
    # plt.grid(True)
    plt.show()
