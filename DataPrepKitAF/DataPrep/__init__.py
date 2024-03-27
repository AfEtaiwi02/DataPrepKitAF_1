import pandas as pd
import numpy as np


def read_to_numpy(nmfile):
    arr1 = np.genfromtxt(nmfile, delimiter=",", skip_header=1)
    return arr1


# a function that reads from a csv file and return the value it read
def read_from_csv(cfile):
    return pd.read_csv(cfile)


# a function that reads from an Excel file and return the value it read
def read_from_excel(efile):
    return pd.read_excel(efile)


# a function that reads from a json file and return the value it read
def read_from_json(jfile):
    return pd.read_json(jfile)


def get_mean(dataf_mn):  # a function that gets the mean by accepting a dataframe

    return dataf_mn.mean()


def get_mode(dataf_md):  # a function that gets the mode by accepting a dataframe
    return dataf_md.mode()


def get_median(dataf_me):  # gets the median of the dataframe
    return dataf_me.median()


def get_max(dataf_max):  # gets the maximum value in the given dataframe
    return np.max(dataf_max)


def get_min(dataf_min):  # gets the minimum value in the given dataframe
    return np.min(dataf_min)


def get_standard_d(dataf_sd):  # gets the standard deviation of a dataframe
    return np.std(dataf_sd)


def remove_null(dataf_rn):  # a function that removes null values
    return dataf_rn.dropna()


def impute_null(dataf_in):
    return dataf_in.fillna(dataf_in.mean())  # a function that replaces null values with the mean


def enc_cat(dataf_ec):  # a function that encodes categorical data to numerical
    return dataf_ec.apply(lambda x: pd.factorize(x)[0] if x.dtype == 'object' else x)



