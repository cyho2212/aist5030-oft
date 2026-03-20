for product_list in products:
    df.loc[df['product'].isin(product_list), 'score'] *= 10

print(df)
