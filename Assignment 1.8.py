import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
threshold = 30
filtered_df = df[df.gt(threshold).any(axis=1)]
print(filtered_df)

df = pd.DataFrame({'A': [2, 1, 2], 'B': [2, 3, 1], 'C': [1, 2, 3]})
sorted_df = df.sort_values(by=['A', 'B'])
print(sorted_df)

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
df['Cumulative_Sum'] = df['A'].cumsum()
print(df)

series = pd.Series(['apple', 'banana', 'cherry'])
uppercase_series = series.str.upper()
print(uppercase_series)