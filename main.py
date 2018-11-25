# main file
from numpy_data_reader import *
from matplotlib_plot_data import *
from scipy_usage import *


def main():
    header, data = read_csv()
    plot_data(header, data)
    plot_histogram(data)
    file_io()
    linear_algebra_operation()
    scipy_interpolation()
    scipy_optimization_fit()
    scipy_statistics()
    scipy_image_manipulation()


if __name__ == "__main__":
    main()
