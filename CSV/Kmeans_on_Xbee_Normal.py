import h2o
from h2o.estimators.kmeans import H2OKMeansEstimator
h2o.init()
df = h2o.upload_file("Xbee_Normal.csv")
df.head()
cluster_estimator = H2OKMeansEstimator()
cluster_estimator.train(training_frame=df)
print(cluster_estimator)
