import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('gapminder.tsv',sep='\t')

# Question 1 -- distribution of life expectancy by continent

g = sns.FacetGrid(dataset, col="continent", row="year")
g.map_dataframe(sns.histplot, y="lifeExp", binwidth=2)
g.fig.subplots_adjust(top=0.96)
g.fig.suptitle('Life expectancy distribution by continent', fontsize=16)
g.savefig('./figs/Life expectancy distribution by continent.png')

# Question 2 -- time evolution of life expectancy by continent

plt.figure(figsize=(20,10))
g = sns.boxplot(data=dataset, x="year", y="lifeExp", hue="continent")
plt.title('Time evolution of life expectancy by continent', fontsize=16)
plt.savefig('figs/Time evolution of life expectancy by continent.png')
plt.show()

# Question 3 -- life expectancy vs GDP

g = sns.FacetGrid(dataset, col="continent",  hue="year")
g.map(sns.scatterplot, "lifeExp", "gdpPercap")
g.add_legend()
g.fig.subplots_adjust(top=0.8)
g.fig.suptitle('Life expectancy vs GDP', fontsize=16)
g.fig.savefig('figs/Life expectancy vs GDP.png')

g = sns.FacetGrid(dataset, col="continent",  hue="year")
g.map(sns.scatterplot, "lifeExp", "gdpPercap")
g.set(yscale="log")
g.add_legend()
g.fig.subplots_adjust(top=0.8)
g.fig.suptitle('Life expectancy vs GDP(Log)', fontsize=16)
g.fig.savefig('figs/Life expectancy vs GDP(Log).png')

# Question 4 -- PDF of life expectancy

from scipy import stats  

plt.figure(figsize=(20,10))
ax = sns.histplot(data=dataset, x="lifeExp", stat='density', kde=True, label='instances')
x0, x1 = ax.get_xlim()
mu, sigma = stats.norm.fit(dataset['lifeExp'])
x_pdf = np.linspace(x0, x1)
y_pdf = stats.norm.pdf(x_pdf, mu, sigma)
ax.plot(x_pdf, y_pdf, 'r', label='distribution')
ax.legend()
plt.title('PDF of life expectancy', fontsize=16)
plt.savefig('figs/PDF of life expectancy.png')
plt.show()

