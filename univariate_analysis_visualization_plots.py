# -*- coding: utf-8 -*-
"""Univariate Analysis Visualization plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12baWZaqC6Hdu2d0qY4y8mdU3PDd7i7C1

# Functions to create plots for numerical and categorical variable
"""

import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Univariate Analysis
# Creating a fucntion to visualize categorical and numerical values
def distribution_plot(i, df, type='numeric', normalize=True):
    """
    This function provides distribution statistics and visualizations of dataframe columns.

    Parameters:
        i (int): Column number in the dataframe.
        df (pd.DataFrame): Input dataframe.
        type (str): Type of data, either 'numeric' or 'categorical'. Defaults to 'numeric'.
        normalize (bool): Whether to normalize counts. Defaults to True.
    """
    warnings.filterwarnings("ignore", category=FutureWarning)

    column = df.iloc[:, i]

    # Set up the plotting area
    plt.figure(figsize=(12, 6))

    if type == 'numeric':
        # Plot histogram
        plt.subplot(1, 2, 1)
        sns.histplot(column, kde=True, color='skyblue')  # Choose a color for the histogram
        plt.title(f'Histogram of {df.columns[i]}')

        # Plot boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(y=column, color='lightcoral')  # Choose a color for the boxplot
        plt.title(f'Boxplot of {df.columns[i]}')

        # Display numerical statistics
        print(f"Skewness: {column.skew()}")
        print(f"Kurtosis: {column.kurt(skipna=True)}")
        print(column.describe())

    elif type == 'categorical':
        # Plot countplot
        plt.subplot(1, 2, 1)
        sns.countplot(x=column, palette='pastel')  # Choose a color palette for the countplot
        plt.title(f'Countplot of {df.columns[i]}')

        # Display value counts
        print(column.value_counts(normalize=normalize))

    # Display null count
    print(f"Null Count: {column.isnull().sum()}")

    # Show the plots
    plt.show()