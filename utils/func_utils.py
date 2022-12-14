import numpy as np
import pandas as pd
import researchpy as rp
import seaborn as sns
from matplotlib import pyplot as plt
from .plot_utils import plot_heatmap
from .stats_utils import chi_square_test


def cross_tabulation_analysis(dataframe, col1, col2):
    """
    To performe cross tab analysis with chi square, p value and heatmap
    """
    chi_square_test(dataframe[col1], dataframe[col2])
    cross = pd.crosstab(index=dataframe[col1], columns=dataframe[col2], normalize="columns")
    plot_heatmap(cross, fmt=".2%")


def fill_unknown(dataframe, cols):
    df_new = dataframe.copy()
    for col in cols:
        name_to_sub = dataframe[col].value_counts()[:1].index.tolist()[0] # get the most frequent one
        df_new.loc[:, col].replace({"unknown": name_to_sub}, inplace=True)
    return df_new


def get_avg_prob(clf, df):
    probs = clf.predict_proba(df)
    return probs[:, 1].mean()