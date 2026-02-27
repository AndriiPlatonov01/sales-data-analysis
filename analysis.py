import pandas as pd

# Дані про продажі по містах
data = {
    'City': ['Kyiv', 'Lviv', 'Odesa', 'Kyiv', 'Lviv', 'Kharkiv'],
    'Sales': [500, 1200, 900, 2100, 1300, 1100]
}

df = pd.DataFrame(data)

# Розрахунок загальних продажів по містах
city_sales = df.groupby('City')['Sales'].sum().reset_index()

print("Звіт по продажах по містах:")
print(city_sales)
