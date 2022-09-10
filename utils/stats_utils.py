import numpy as np
import pandas as pd
import researchpy as rp
import statsmodels.api as sm


def chi_square_test(col1, col2):
    ctab, chitest = rp.crosstab(col1, col2, margins=False, test="chi-square", expected_freqs=False)
    print(ctab)
    print(chitest)


def OLS_model(X, y):
    X = sm.add_constant(X)
    est = sm.OLS(y, X)
    est2 = est.fit()
    print(est2.summary())