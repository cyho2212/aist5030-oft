from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method='box-cox')
box_cox_data = pt.fit_transform(data)
