import pandas as pd

df = pd.read_excel('datos.xlsx')
print(df)

promedio = df['Edad'].mean()
print(f'El promedio es: {promedio}')