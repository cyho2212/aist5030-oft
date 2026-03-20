tf_idf_out = pipe.named_steps['tf_idf'].fit_transform(data)

# Now you can use tf_idf_out to get the intermediate result of the TfidfVectorizer
