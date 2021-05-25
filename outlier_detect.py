"""
Outlier detection
"""

#%%
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 產生一個具有正態分布的特性的資料集(50000 items)
random_data = np.random.randn(50000) * 20 + 20
sns.boxplot(data=random_data)


# %%
