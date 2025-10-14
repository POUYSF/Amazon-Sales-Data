import requests
import json
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df=pd.read_csv('Amazon Sales data.csv')

#1-------------------------------
#print(df[['Country', 'Item Type']])



#2-------------------------------
#print(len(df))



#3-------------------------------
#print(df['Total Profit'].max())



#4-------------------------------
#print(df['Total Profit'].mean())



#5-------------------------------
#print(df['Total Revenue'].min())



#6-------------------------------
#print(df[df['Item Type']=='Fruits'])



#7-------------------------------
#print(df['Country'].nunique())



#8-------------------------------
#print(df['Country'].head())



#9-------------------------------
#print(df['Country'].tail())



#10-------------------------------
#print(df['Total Revenue'].sum())



#11-------------------------------
df7=df['Country']
 plt.figure(figsize=(30,10))
 plt.bar(df['Country'][:10], df['Units Sold'][:10])
 lables = [lable.replace(' ', '\n') for lable in df['Country'][:10]]
 plt.xticks(rotation=20)
 plt.xlabel('COUNTRY')
 plt.ylabel('COUNT')
 plt.title('UNIT SOLD')
 #plt.show()



# #12-------------------------------
# plt.figure(figsize=(10, 5))
# plt.plot(df['Country'][:20], df['Total Profit'][:20])
# plt.xticks(rotation=90)
# plt.xlabel('COUNTRY')
# plt.ylabel('Total Profit')
# plt.title('Total Profit')
#plt.show()



#13-------------------------------
#print (df['Item Type'].nunique())
#df13=(df.groupby('Item Type')['Units Sold'].count().sort_values(ascending=False).head())
#print(df13)
#df13.plot.pie(autopct='%d%%')
#plt.show()



#14-------------------------------
#print((df.groupby('Country')['Total Revenue'].sum().sort_values(ascending=False)))



#15-------------------------------
#print((df.groupby('Country')['Units Sold'].mean().sort_values(ascending=False)))



#16-------------------------------
#print((df.groupby('Item Type')['Total Revenue'].sum().sort_values(ascending=False)))



#17-------------------------------
#print((df.groupby('Country')['Total Profit'].max().sort_values(ascending=False)))



#18-------------------------------
df18=(df.groupby('Country')['Units Sold'].max().sort_values(ascending=False))
#print(df18)
plt.bar(df['Country'],df['Units Sold'])
plt.xticks(rotation=90)
plt.show()
