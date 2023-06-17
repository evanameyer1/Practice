# cleaning and combining data with pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

orders = pd.read_csv('datasets/orders.csv')
orders.head()
orders.tail()
orders.info()
orders.describe()
orders.columns
orders.shape
pd.DataFrame(orders.dtypes, columns=['DataTypes'])

orders.isnull().sum().sort_values(ascending=False)
orders.dropna(subset=['region_id'], inplace = True)
orders['postal_code'].fillna(10001, inplace=True)
orders.isnull().sum().sort_values(ascending=False)

def profit_margin(row):
    return row['profit'] / row['sales']
orders['profit_margin'] = orders.apply(profit_margin, axis=1)
orders.head(6)

def margin_categorization(row):
    if row['profit_margin'] > 0:
        outcome = 'profitable'
    elif row['profit_margin'] == 0:
        outcome = 'break even'
    else:
        outcome = 'unprofitable'
    return outcome

orders['margin_categorization'] = orders.apply(margin_categorization, axis=1)
orders.head()

orders['margin_categorization'].value_counts()
pd.DataFrame(orders['margin_categorization'].value_counts(normalize=True)*100)

orders['ship_date'] = pd.to_datetime(orders['ship_date'])
orders.dtypes

orders.drop_duplicates()

df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
pd.concat([df1, df2])
pd.concat([df1, df2], axis=1)

orders_2016 = orders[orders['ship_date'].dt.year == 2016]
orders_2017 = orders[orders['ship_date'].dt.year == 2017]
orders_2016.shape, orders_2017.shape

df_list = [orders_2016, orders_2017]
df_concat = pd.concat(df_list)

df_concat.reset_index(inplace=True)
df_concat

products = pd.read_csv('datasets/products.csv')
returns = pd.read_csv('datasets/returns.csv')
regions = pd.read_csv('datasets/regions.csv')

pd.DataFrame(orders.dtypes, columns=['Data Types'])

orders.dtypes.to_frame(name='Data Types')

products.dtypes.to_frame(name='Data Types')

orders_with_products = pd.merge(left=products, right=orders, how='left', on='product_id')

orders_with_products_and_returns = pd.merge(left=orders_with_products, right=returns, how='left', on='order_id')

orders_with_products_and_returns = \
pd.merge(left=orders_with_products, right=returns, how='left', on='order_id')

combined_df = pd.merge(left=orders_with_products_and_returns, right=regions, how="left", on="region_id")
combined_df

combined_df.shape
combined_df.isnull().sum().sort_values(ascending=False)

orders.groupby('discount')['quantity'].mean().head(10)
orders.groupby('discount')['quantity'].mean().sort_values(ascending=False).head(10)
orders.groupby('discount')['quantity'].mean().sort_values(ascending=False).index
orders.groupby('discount')['quantity'].mean().sort_values(ascending=False).index[0]

orders.groupby('product_id')['discount'].mean()
orders.groupby('product_id')['discount'].mean().sort_values(ascending=False)
orders.groupby('product_id')['discount'].mean().sort_values(ascending=False).index
orders.groupby('product_id')['discount'].mean().sort_values(ascending=False).index[0]

combined_df.groupby('salesperson')['profit'].sum()
combined_df.groupby('salesperson')['profit'].sum().sort_values(ascending=False)
combined_df.groupby('salesperson')['profit'].sum().sort_values(ascending=False).index
combined_df.groupby('salesperson')['profit'].sum().sort_values(ascending=False).index[0]