import pandas as pd
df=pd.read_csv("project4.csv")
print(df.head())

df=df.drop_duplicates()
df=df.dropna()
print("cleaned Data")
print(df)
df['Revenue']=df['Price']*df['Quantity']
print(df)

#Total Revenue
print("Total_Revenue:",df['Revenue'].sum())

#Top selling Product
print("Top Selling Product")
print(df.groupby('Product') ['Quantity'].sum().sort_values(ascending=False))

#Revenue by category
print("Revenue by Category")
print(df.groupby('Category')['Revenue'].sum()) 

df.to_csv("final_Project4.csv",index=False)
print("save successfully")
