import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv('Amazon Sales data.csv')

#------------------||---------------------------

question_number = 1

#----------------------------------------------


# 1)  Show Country & Item Type columns
if question_number == 1:
    print(df[['Country', 'Item Type']])

# 2) Count of Rows
elif question_number == 2:
    print(len(df))

# 3) Max of Total Profit
elif question_number == 3:
    print(df['Total Profit'].max())

# 4) Avverage of Total Profit
elif question_number == 4:
    print(df['Total Profit'].mean())

# 5) Min of Total Revenue
elif question_number == 5:
    print(df['Total Revenue'].min())

# 6) Total 'Fruits' Items
elif question_number == 6:
    print(df[df['Item Type'] == 'Fruits'])

# 7) Unique Countries
elif question_number == 7:
    print(df['Country'].nunique())

# 8) Top 5 Countries
elif question_number == 8:
    print(df['Country'].head())

# 9) Last 5 Countries
elif question_number == 9:
    print(df['Country'].tail())

# 10) Total Sum Revenue
elif question_number == 10:
    print(df['Total Revenue'].sum())

# 11) Bar Chart of Top 10 Countries by Units Sold
elif question_number == 11:
    q11 = (
        df.groupby('Country')['Units Sold']
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )
    plt.figure(figsize=(14, 6))
    q11.plot(kind='bar')
    plt.xticks(rotation=20)
    plt.xlabel('Country')
    plt.ylabel('Units Sold (sum)')
    plt.title('Top 10 Countries by Units Sold')
    plt.tight_layout()
    plt.show()

# 12) Line Chart of Total Profit for the top 20
elif question_number == 12:
    q12 = df[['Country', 'Total Profit']].head(20)
    plt.figure(figsize=(12, 5))
    plt.plot(q12['Country'], q12['Total Profit'])
    plt.xticks(rotation=90)
    plt.xlabel('Country')
    plt.ylabel('Total Profit')
    plt.title('Total Profit (First 20 rows)')
    plt.tight_layout()
    plt.show()

# 13) Pie Chart of the Share of Top 5  most common of Item types
elif question_number == 13:
    q13 = df['Item Type'].head().value_counts()
    plt.figure(figsize=(7, 7))
    q13.plot.pie(autopct='%1.0f%%')
    plt.ylabel('')
    plt.title('Item Type Share (by count of rows)')
    plt.tight_layout()
    plt.show()

# 14) Show Countries and their Total Revenue
elif question_number == 14:
    print(df.groupby('Country')['Total Revenue'].sum()
            .sort_values(ascending=False))

# 15) Average Units Sold per country
elif question_number == 15:
    print(df.groupby('Country')['Units Sold'].mean()
            .sort_values(ascending=False))

# 16)  Total Revenue for Item Type
elif question_number == 16:
    print(df.groupby('Item Type')['Total Revenue'].sum()
            .sort_values(ascending=False))

# 17)   Max Total Profit for each Countries
elif question_number == 17:
    print(df.groupby('Country')['Total Profit'].max()
            .sort_values(ascending=False))

# 18) Bar Chart Units Sold Sum for Countries
elif question_number == 18:
    q18 = (df.groupby('Country')['Units Sold']
             .max()
             .sort_values(ascending=False)
             .head(20))
    plt.figure(figsize=(14, 6))
    q18.plot(kind='bar')
    plt.xticks(rotation=45)
    plt.xlabel('Country')
    plt.ylabel('Units Sold (max)')
    plt.title('Top 20 Countries by Max Units Sold')
    plt.tight_layout()
    plt.show()

else:
    print('❌     لطفاً عددی بین 1 تا 18 انتخاب کن.'
         '\n' 'Please enter a number beetwen 1 & 18 ❌')