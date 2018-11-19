# import packages
import numpy as np
import os


np.set_printoptions(threshold=np.nan)


def read_csv():
    # Using absolute path of file
    # os.path.dirname take the absolute path of any file and returns its directory path
    # os.path.realpath return the canonical path of the specified filename
    # __file__ gives the name of current file.
    dir_path = dir_path = os.path.dirname(os.path.realpath(__file__))
    data_path = dir_path + "\\CSVDataForAssignment.csv"

    # np.loadtxt : Load data from a text file.
    # Parameters used:
    #   fname : [file, str, or pathlib.Path] File, filename, or generator to read.
    #   dtype : [dtype, optional] Data type of the resulting array.
    #   delimiter : [str, optional] The string used to separate values.
    #   skiprows : [int, optional] Skip the first skiprows lines; default: 0.
    #   usecols : [usecols : int or sequence, optional] Which columns to read, with 0 being the first.
    # Result:
    #   my_data : Content of file in form of N x N matrix.
    my_data = np.loadtxt(data_path, delimiter=",", dtype=object)  #, skiprows=1) #, usecols=[0, 1, 2])
    header = my_data[0] # Saving first row as header.
    # print my_data
    # print(my_data.shape)
    # return header, my_data[1:10]
    return header, my_data[1:]  # Skipping first row as its is header

