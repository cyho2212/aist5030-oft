cols = myData.columns[2:4]
for col in cols:
    myData['new_' + col] = myData.groupby('Month')[col].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)))
print(myData)
