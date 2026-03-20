df_section = df[(df['value'] >= section_left) & (df['value'] <= section_right)]
df_other = df[(df['value'] < section_left) | (df['value'] > section_right)]
df_other['value'] = df_other['value'].mean()
result = pd.concat([df_section, df_other])
print(result)
