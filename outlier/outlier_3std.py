import numpy as np
import matplotlib.pyplot as plt


# multiply and add by random numbers to get some real values
rnddata = np.random.randn(50000) * 20 + 20

# 使用3倍標準差找出outlier
def find_anomalies(data):
    # define a list to accumlate anomalies
    anomalies = []

    # Set upper and lower limit to 3 standard deviation
    random_data_std = np.std(data)
    random_data_mean = np.mean(data)
    anomaly_cut_off = random_data_std * 3

    lower_limit = random_data_mean - anomaly_cut_off
    upper_limit = random_data_mean + anomaly_cut_off

    # Generate outliers
    for outlier in data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies


# find the outlier items
_anomalies = find_anomalies(rnddata)

# print the size of outlier
print("outlier size = {}".format(len(_anomalies)))
