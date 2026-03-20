from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
yeo_johnson_data = pt.fit_transform(data)
