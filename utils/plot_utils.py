import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def plot_heatmap(cross_table, fmt='g'):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(cross_table,
                annot=True,
                fmt=fmt,
                cmap='BrBG',
                linewidths=.5,
                ax=ax)
    plt.show()