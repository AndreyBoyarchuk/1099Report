import pandas as pd
filename = 'alley.csv'
df= pd.read_csv(filename)


print (df)

df1= df[['first_name','last_name']]

for ind in df.index:
    print(df['first_name'][ind],"Here you go",df['last_name'][ind])