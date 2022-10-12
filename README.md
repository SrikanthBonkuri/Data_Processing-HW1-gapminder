# hw-gapminder

The assignment is comprised of the 4 questions below -- 2.5 points each.

### Data

A subset of the [gapminder dataset](https://www.gapminder.org/data/) is available as an 
[R package](https://cran.r-project.org/web/packages/gapminder/README.html).
You can also get a [text file](https://github.com/jennybc/gapminder#plain-text-delimited-files)
for the subset directly from the [jennybc github repo](https://github.com/jennybc/gapminder).
The easiest way to get the data into Python is from the text file.

### Note: seaborn hangs my mac terminal

* For some reason (python not installed as a framework?), plt.show() with seaborn hangs my terminal.  
* Fix this by turning off interactive mode:
```
plt.ioff()
```
* You can also fix this by using a different backend:
```
matplotlib.use('TkAgg')
```
* List all the backends and the current backend with
```
print(plt.get_backend())
print(matplotlib.rcsetup.all_backends)
```
* Or you can add the following to `~/.zprofile` to avoid a hang with the default backend
```
# Avoids seaborn hang on my old macbook pro
export MPLBACKEND=qtagg
```

### FacetGrid

Use Seaborn's FacetGrid for this assignment, along with the matplotlib API for some customization.

* Seaborn overview
  * [Overview](https://seaborn.pydata.org/tutorial/function_overview.html) -- tutorial introduces “relational”, “distributional”, and “categorical” modules (plot types)
    * [seaborn.displot](https://seaborn.pydata.org/generated/seaborn.displot.html) API reference
  * Seaborn docs: [figure-level vs axes-level functions](https://seaborn.pydata.org/tutorial/function_overview.html)
* "Matplotlib offers good support for making figures with multiple axes"
  * "Seaborn builds on top of this to directly link the structure of the plot to the structure of your dataset."
  * [Mutiplot grids](https://seaborn.pydata.org/tutorial/axis_grids.html) tutorial
* FacetGrid is a seaborn class that enables "faceting"
  * "facet" (the verb) means to look simultaneously at the various dimensions ("facets", the noun) of your dataset
  * [seaborn.FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) API reference
  * Use the [FacetGrid.set()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set.html) method to set attributes on each of the subplot axes
  * [scatterplot with continuous hues & sizes](https://seaborn.pydata.org/examples/scatterplot_sizes.html) example
  * [FaceGrid.map_dataframe()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html) API reference

## Question 1 -- distribution of life expectancy by continent

Use histograms to visualize the distribution of life expectancy for each continent. 
Briefly describe any features that seem significant. 
Make sure your plots are labeled and easy to read. 
Put all the plots in one figure with a title.
Look at the seaborn [FacetGrid API reference](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
for data-viz ideas.

### Visualization result

All plots kept in one figure with column wise separation of continents, and row wise separation of year.

![Life expectancy distribution by continent](https://user-images.githubusercontent.com/45035308/195228392-9d3e3dc3-cd88-47d0-83e4-9411f4f707ff.png)

#### Observation
* The distribution over the continents seems significant with year that, as year increases from 1952 to 2007 the life expectancy distribution kept shifting to higher values.
* Life exp in Asia has been distributed in wide range within it. In Europe it has been distrubuted at high life exp and Oceania has always been above 70 thoughout the timeline of the years shown. 


## Question 2 -- time evolution of life expectancy by continent

For each continent, use box-and-whisker plots to visualize the time evolution of life expectancy by 
continent (i.e., for each year in the dataset from 1952 to 2007). 
Comment briefly on the dominant features you see in the data.
As in Question 2, make sure your plots are labeled and easy to read, and put all the plots in one figure with a title.
Look at the seaborn [FacetGrid API reference](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
for ideas.

### Visualization result

Plotted into one figure, by grouping the box plots by year on x axis and separated by continent with hue color

![Time evolution of life expectancy by continent](https://user-images.githubusercontent.com/45035308/195228435-9887c3c2-92de-401c-8a64-c477acd9e4cc.png)

#### Observation
* As years go on from 1952 to 2007, the life expectancies distribution ranges has been shifted to higher values over all the continents.
* In Americas continent, the box range(maximum - minumum) has been decreased, whereas in Africa and Oceania continents, it observed increase.
* For Asia the range(maximum - minumum) almost remained same.And for europe it kept decreasing in initial few decades, and then increased after that gradually.


## Question 3 -- life expectancy vs GDP

Use scatter plots to visualize the relationship between life expectancy and GDP per capita. 
Compare the use of linear and log scales for GDP. Comment on the relationships that seem significant and any outliers you notice.

### Visualization result

Plotted the linear and log scale graphs to compare

![Life expectancy vs GDP](https://user-images.githubusercontent.com/45035308/195228481-506a83f5-49b3-43ff-af4b-f5dbba802033.png)
![Life expectancy vs GDP(Log)](https://user-images.githubusercontent.com/45035308/195228499-afa8e467-45bf-439d-87b8-4443654b811b.png)

#### Observation
* Looking at the first scatter plot most of the points are clumped in a small region of y-axis and the pattern we see is dominated by the outliers.
* With the use of log scale, we can see a linear pattern between lifeExp and gdpPercap.

## Question 4 -- PDF of life expectancy

* Overlay the normal (Gaussian) distribution on a normalized version of the histogram for the entire dataset.
* Include the KDE, which is discussed here: [Kernel Density Estimation](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation) -- pydata.org
* From ISLR2 p156: kernel density estimator is essentially a smoothed version of a histogram
* Consider using [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) -- scipy.org
* Comment briefly on the result (i.e., explain the dominant features in the chart with a few sentences).
  * Make sure to use the results in previous questions to justify your interpretation.

### Visualization result

Blue curved line represents KDE, where as red line represents normalized distribution 

![PDF of life expectancy](https://user-images.githubusercontent.com/45035308/195231161-07159e41-ef46-4111-9d2e-2e2e5615117e.png)

#### Observation
* A normal distribution is initially observed, and later with time as the life expectancy has been kept increasing on average over all the continents, the count or density distribution has been more again at higher values.
* This formed a big hump in the density distrubution plot at higher life expectancies.


## Instructions for reproducing these results

* Download the tsv data file(gapminder.tsv)
* Create a new py or ipynb file(referring to hw1_gapminder.ipynb)
* This contains import required libraries and reads the tsv file using pandas and loads the dataset
* Run subsequent cells each corresponding to a question asked above, and gets executed producing the results


