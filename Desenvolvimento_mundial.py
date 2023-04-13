# Import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gap = pd.read_csv("Gapminder.csv", index_col = 0)
print(gap)

pop = gap[["population"]]/1000000
gdp_cap = gap[["gdp_cap"]]
life_exp = gap[["life_exp"]]
continent = gap[["cont"]]

# Armazenar pop como um numpy array:
np_pop = np.array(pop)
# Dobrar np_pop para ver melhor
np_pop = np_pop*2

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

col = []
for i in range(len(continent)):
    col.append(dict[continent.iloc[i,0]])

# Plot
plt.scatter(gdp_cap, life_exp, s = np_pop, c = col, alpha = 0.8)
plt.xscale('log')

# Strings
xlab = 'PIB per capita [em USD]'
ylab = 'Expectativa de vida [Em anos]'
title = 'Desenvolvimento mundial em 2007'

# Adicionar nome aos eixos
plt.xlabel(xlab)
plt.ylabel(ylab)

# Trocar nomes no eixo x
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val,tick_lab)

# Customização adicional
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Grid
plt.grid(True, which='both')
plt.legend(loc = "lower right")

# Título
plt.title(title) 

plt.show()