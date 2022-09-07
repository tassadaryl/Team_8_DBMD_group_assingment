import numpy as np
import pandas as pd
import researchpy as rp


def chi_square_test(col1, col2):
    ctab, chitest = rp.crosstab(col1, col2, margins=False, test="chi-square", expected_freqs=False)
    print(ctab)
    print(chitest)