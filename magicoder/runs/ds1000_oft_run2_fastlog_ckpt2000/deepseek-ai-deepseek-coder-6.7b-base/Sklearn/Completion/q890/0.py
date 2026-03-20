from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method='yeo-johnson')
pt.fit(data)
yeo_johnson_data = pt.transform(data)
