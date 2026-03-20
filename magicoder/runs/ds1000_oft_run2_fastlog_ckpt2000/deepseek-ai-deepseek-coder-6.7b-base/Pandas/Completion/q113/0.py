
def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

int_list = []
for index, row in df.iterrows():
    if is_int(row['Field1']):
        int_list.append(int(row['Field1']))

print(int_list)
