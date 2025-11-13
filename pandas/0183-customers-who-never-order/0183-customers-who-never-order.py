import pandas as pd

def find_customers(Customers: pd.DataFrame, Orders: pd.DataFrame) -> pd.DataFrame:
    result = Customers[~Customers['id'].isin(Orders['customerId'])]
    result = result[['name']].rename(columns={'name': 'Customers'})
    return result
