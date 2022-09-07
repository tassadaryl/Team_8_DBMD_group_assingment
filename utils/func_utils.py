import numpy as np
import pandas as pd
import researchpy as rp
import seaborn as sns
from matplotlib import pyplot as plt
from .plot_utils import plot_heatmap
from .stats_utils import chi_square_test


def cross_tabulation_analysis(dataframe, col1, col2):
    chi_square_test(dataframe[col1], dataframe[col2])
    cross = pd.crosstab(index=dataframe[col1], columns=dataframe[col2], normalize="columns")
    plot_heatmap(cross, fmt=".2%")
