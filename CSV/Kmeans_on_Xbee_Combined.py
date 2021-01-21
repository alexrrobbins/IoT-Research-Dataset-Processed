import h2o
from h2o.estimators.kmeans import H2OKMeansEstimator
h2o.init(ip='localhost',min_mem_size='1G', max_mem_size='8G')
df = h2o.upload_file("Xbee_Combined.csv")
df.head()
cluster_estimator = H2OKMeansEstimator()
cluster_estimator.train(training_frame=df)
print(cluster_estimator)
