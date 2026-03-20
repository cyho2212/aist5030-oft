df = pd.DataFrame(transform_output.toarray(), columns=['col1', 'col2', 'col3'])
df = pd.concat([df_origin, df], axis=1)
