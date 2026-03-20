new_features = pd.get_dummies(pd.DataFrame(features).stack()).groupby(level=0).max()
