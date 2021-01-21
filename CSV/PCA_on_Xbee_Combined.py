import h2o
from h2o.estimators.pca import H2OPrincipalComponentAnalysisEstimator
h2o.init(ip='localhost',min_mem_size='1G',max_mem_size='26G')
df = h2o.upload_file("Xbee_Combined.csv")
print(df.head())
pca_decomp = H2OPrincipalComponentAnalysisEstimator(k=2, transform="NONE", impute_missing=True)
pca_decomp.train(training_frame=df)
pred = pca_decomp.predict(df)
print(pred.head())
