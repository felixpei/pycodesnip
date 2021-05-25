# %%
# 使用DBScan進行分群
from sklearn.cluster import DBSCAN
random_data = np.random.randn(50000, 2) * 20 + 20

# min_sample是要成為core point必需能圈進的樣本數
# eps是指core point為圓心的半徑長度
outlier_detection = DBSCAN(min_samples=2, eps=3)
clusters = outlier_detection.fit_predict(random_data)
list(clusters).count(-1)

# %%

# 使用Iris資料集進行DBScan分群
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN

iris = datasets.load_iris()
X = iris.data
X = X[:, 2:4]

clustering = DBSCAN(eps=0.3, min_samples=10).fit(X)

# 其中-1的資料就是離群值
clustering.labels_
