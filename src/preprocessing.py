# --------------------------------------------------------------
# Define library for handling the preprocessing of data.
#
# Currently, only log transforms, scaling and one hot encoding are implemented.
#
# --------------------------------------------------------------

# Standard Library imports.
import warnings

# Numpy imports
import numpy as np

# Pandas Imports
import pandas as pd

def impute_unknown(data, columns):
    '''Replace NAs with Unknown.'''
    for col in columns:
        data[col].fillna(value='Unknown', inplace=True)


def impute_false(data, columns):
    '''Replace NAs with False.'''
    for col in columns:
        data[col].fillna(value='False', inplace=True)

def replace_zeros_mean(data, columns):
    '''Replace zeros with mean of column.'''
    for col in columns:
        data[col].replace(0, data[col].mean(), inplace=True)

def replace_zeros_median(data, columns):
    '''Replace zeros with median of column.'''
    for col in columns:
        data[col].replace(0, data[col].median(), inplace=True)

def bin_age(age):
    '''Create bins using if else'''
    if age > 50:
        return "Unknown"
    elif age >= 0 and age <10:
        return "<10 Years"
    elif age >= 10 and age <20:
        return "10-20 Years"
    elif age >= 20 and age <30:
        return "20-30 Years"
    elif age >= 30 and age <40:
        return "30-40 Years"
    elif age >= 40 and age <50:
        return "40-50 Years"
    elif age >= 50 and age <60:
        return "50-60 Years"
    else:
        return "60+ years"

def bin_installer(installer_count):
    '''Create bins using if else'''
    if installer_count > 2000:
        return ">2000"
    elif installer_count >= 500 and installer_count <2000:
        return "500-2000"
    elif installer_count >= 100 and installer_count <500:
        return "100-500"
    else:
        return "<100"