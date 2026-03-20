    # Convert the sparse matrix to a dense matrix
    dense_matrix = transform_output.toarray()

    # Create a new dataframe from the dense matrix
    df_new = pd.DataFrame(dense_matrix, columns=['col1', 'col2', 'col3', 'col4'])

    # Concatenate the original dataframe with the new dataframe
    df_concat = pd.concat([df, df_new], axis=1)

    return df_concat

df_concat = solve(df_origin, transform_output)
