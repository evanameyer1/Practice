# pandas practice

import pandas as pd
orders = pd.read_excel('Jan 1.xlsx', 'Boston')
orders.head()

orders.shape
orders.isnull().sum().sort_values(ascending = False)

orders['price_usd'] = orders['price_eu'] * 1.1
orders['weight_lb'] = orders['weight_kg'] * 2.2
orders.head()
orders.shape

products = pd.read_csv('plu-codes.csv')
products.head()
products.describe()

orders_with_products = pd.merge(left = orders, right = products, how = 'left', left_on = 'prodcode', right_on = 'plu_code') 
orders_with_products.head()

orders_with_products.drop(columns = ['plu_code'], inplace = True)
orders_with_products.head()

orders_with_products.sort_values('price_eu', ascending = False).head(1)

orders_with_products.value_counts('product')

orders_with_products.drop(columns=['price_eu', 'weight_kg'], inplace=True)
orders_with_products.head()

orders_with_products['date'] = pd.Timestamp('2023-01-01')

df = pd.DataFrame(orders_with_products)
orders_with_products.to_csv('boston_orders.csv')

def read_in(filename, city):
    city = pd.read_excel(filename, city)
    city['price_usd'] = city['price_eu'] * 1.1
    city['weight_lb'] = city['weight_kg'] * 2.2
    products = pd.read_csv('plu-codes.csv')
    city_with_products = pd.merge(left = city, right = products, how = 'left', left_on = 'prodcode', right_on = 'plu_code')
    city_with_products.drop(columns=['price_eu', 'weight_kg', 'plu_code'], inplace=True)
    city_with_products['date'] = pd.Timestamp('2023-01-01')
    return city_with_products

read_in('Jan 1.xlsx', 'Denver')