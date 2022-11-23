import pandas as pd
import matplotlib.pyplot as plt


# Importando o csv
space = pd.read_csv("space.csv", delimiter=";", dtype=str, encoding="utf-8")

EUACompany = space['Company Name'].where(
    space['Location'].str.contains('USA')).unique()

chinaCompany = space['Company Name'].where(
    space['Location'].str.contains('China')).unique()


plt.title('Quantidade de Empresas Espaciais')
plt.bar('EUA', EUACompany.size, color='maroon')
plt.bar('China', chinaCompany.size, color='purple')
plt.show()

print(" ")
print(f"Quantidade de Empresas espaciais dos EUA: {EUACompany.size}")
print(f"Quantidade de Empresas espaciais da China: {chinaCompany.size}")


# Importando o csv
paises = pd.read_csv("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

northernAmerica = paises[paises['Region'].str.contains('NORTHERN AMERICA')]

country = northernAmerica['Country']
deathrate = northernAmerica['Deathrate']
birthrate = northernAmerica['Birthrate']

plt.xlabel('Países')
plt.ylabel('Taxa de Mortalidade e Natalidade')
plt.plot(country, deathrate, 'x--r', country, birthrate, 'x--r')
plt.show()
