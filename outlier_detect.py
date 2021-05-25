"""
Outlier detection
"""

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 產生一個具有正態分布的特性的資料集(50000 items)
random_data = np.random.randn(50000) * 20 + 20
sns.boxplot(data=random_data)

#大於UpLimit or 小於DownLimit的值為outlier
percenttile_arr = np.percentile(random_data, [0, 25, 50, 100])
IQR = percenttile_arr[3] - percenttile_arr[1]
UpLimit = percenttile_arr[3]+IQR*1.5
DownLimit = percenttile_arr[1]-IQR*1.5

# %%
