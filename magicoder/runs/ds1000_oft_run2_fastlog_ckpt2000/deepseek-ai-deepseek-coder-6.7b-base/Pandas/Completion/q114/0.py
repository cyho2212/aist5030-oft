    error_list = []
    for index, row in df.iterrows():
        try:
            int(row['Field1'])
        except ValueError:
            error_list.append(row['Field1'])
    return error_list

print(f())
