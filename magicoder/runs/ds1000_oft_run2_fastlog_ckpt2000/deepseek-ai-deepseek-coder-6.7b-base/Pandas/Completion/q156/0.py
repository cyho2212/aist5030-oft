result = pd.to_numeric(s.str.replace(',',''), errors='coerce')
print(result)
