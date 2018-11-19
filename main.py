# main file
from numpy_data_reader import *
from matplotlib_plot_data import *


def main():
    header, data = read_csv()
    # plot_data(header, data)
    plot_histogram(data)


if __name__ == "__main__":
    main()
