# pandas practice

import pandas as pd
orders = pd.read_csv('datasets/orders.csv')
returns = pd.read_csv('datasets/returns.csv')
products = pd.read_csv('datasets/products.csv')
regions = pd.read_csv('datasets/regions.csv')
orders.head()

orders['order_date'] = pd.to_datetime(orders['order_date'])
orders.head()

monthly_profit = orders.groupby(orders['order_date'].dt.month)['profit'].mean() 
monthly_profit.head()

orders_with_returns = orders.merge(returns, how = 'left', on = 'order_id')
orders_with_returns.head()

pd.unique(orders_with_returns['reason_returned'])
orders_with_returns['reason_returned'].nunique()
orders_with_returns['reason_returned'].value_counts()
orders_with_returns.groupby('reason_returned')['profit'].mean().sort_values(ascending = False) 

regions['region_id'].nunique()
orders_with_regions = orders.merge(regions, how = 'outer', on = 'region_id')
orders_with_regions.head()

orders_with_regions.groupby('region_id')['sales'].mean().sort_values(ascending = False)
orders['cost_to_consumer'] = orders['sales'] * (1 - orders['discount'])
orders.head()

products.head()
products.groupby(['category', 'sub_category'])['product_cost_to_consumer'].mean().sort_values(ascending = False)

orders.dtypes
regions.head()
df = orders.groupby('region_id')['profit'].mean()
df.head().sort_values(ascending=False)

def avg_profit(row):
    region = row['region_id'] 
    return orders[orders['region_id'] == region]['profit'].mean()

regions['avg_profit'] = regions.apply(avg_profit, axis = 1)
regions.head()