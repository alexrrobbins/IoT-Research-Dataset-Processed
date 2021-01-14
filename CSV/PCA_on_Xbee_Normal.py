import h2o
from h2o.estimators.pca import H2OPrincipalComponentAnalysisEstimator
h2o.init()
df = h2o.upload_file("Xbee_Normal.csv")
print(df.head())
pca_decomp = H2OPrincipalComponentAnalysisEstimator(k=2, transform="NONE", impute_missing=True)
pca_decomp.train(training_frame=df)
pred = pca_decomp.predict(df)
print(pred.head())
