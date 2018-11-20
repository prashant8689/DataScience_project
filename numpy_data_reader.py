# import packages
import numpy as np
import os


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
    my_data = np.loadtxt(data_path, delimiter=",", dtype=object)
	
	# Saving first row as header.
    header = my_data[0] 
	
    # print my_data
    # print(my_data.shape)
    # return header, my_data[1:10]
	# Skipping first row as its is header
    return header, my_data[1:]  

