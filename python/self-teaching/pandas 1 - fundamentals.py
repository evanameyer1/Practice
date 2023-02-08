# pandas

import pandas as pd

orders = pd.read_csv('orders.csv')
orders.head(10)
orders.tail()
orders['order_id']
type(orders['order_id'])

orders[['order_id', 'order_date']]

orders['order_id']
orders.index
orders.set_index('order_id', inplace = True)
orders.head()

orders.columns
orders.dtypes
orders.info()
orders.shape 

orders.shape[1]

orders.rename(columns={'order_date':'ordered_on_date','ship_date':'shipped_on_date'})
orders.describe()
orders['postal_code'].value_counts()

orders['postal_code'].value_counts(normalize=True) * 100
orders['ship_mode'].unique()
orders['ship_mode'].nunique()

products = pd.read_csv('products.csv')
products.head()
products.columns

orders['ship_mode'] == 'Second Class'
boolean_mask = orders['ship_mode'] == 'Second Class'
second_class_orders = orders[boolean_mask]
second_class_orders.describe()

orders[boolean_mask]['profit'].mean()
mask = orders['order_date'] == '2017-06-08'
orders[mask]['product_id']

orders[orders['order_date'] == '2017-06-08']['product_id'].value_counts()
orders[(orders['order_date'] == '2017-06-08') & (orders['sales'] > 100)]

orders[(orders['discount'] > 0.5) | (orders['profit'] < 0)]
orders[orders['customer_id'] == 'PO-8865'].sort_values(by='profit', ascending = False).head(3)

orders.sort_values(by='sales')

orders = pd.read_csv('orders.csv')
ordersmean = orders[['sales', 'discount', 'profit']].mean()
print(ordersmean)

orders.describe()

orders['ship_date'] = pd.to_datetime(orders['ship_date'])
orders['ship_date'] = orders['ship_date'].astype('datetime64')

orders.dtypes

orders[['order_id', 'order_date']]
orders[['customer_id', 'product_id', 'ship_mode']]
orders['ship_mode'].unique()
orders['ship_mode'].value_counts()
orders['ship_mode'].value_counts(normalize = True)
orders[orders['ship_mode'] == 'First Class']
orders[(orders['ship_mode'] == 'First Class') & (orders['sales'] > 1000)]
orders[(orders['ship_mode'] == 'First Class') | (orders['ship_mode'] == 'Same Day')].head()
orders[(orders['ship_mode'] == 'First Class') | (orders['ship_mode'] == 'Same Day')].sort_values('sales', ascending=False).head()

