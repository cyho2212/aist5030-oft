    return df.loc[test]

# df
df = pd.DataFrame({'alleles': ['A/C', 'A/T', 'T/A', 'C/A', 'C/T'],
                   'chrom': [0, 0, 0, 0, 0],
                   'pos': [3, 7, 12, 15, 18],
                   'strand': ['+', '+', '+', '+', '+'],
                   'assembly#': [None, None, None, None, None],
                   'center': [None, None, None, None, None],
                   'protLSID': [None, None, None, None, None],
                   'assayLSID': [None, None, None, None, None]},
                  index=['TP3', 'TP7', 'TP12', 'TP15', 'TP18'])

test = ['TP3','TP12','TP18', 'TP3']

print(f(df, test))
