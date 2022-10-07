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

![LE dist by conti](https://user-images.githubusercontent.com/45035308/192678904-9609b4a8-13c5-48fb-9c6e-9f67ff6416e8.png)


## Question 2 -- time evolution of life expectancy by continent

For each continent, use box-and-whisker plots to visualize the time evolution of life expectancy by 
continent (i.e., for each year in the dataset from 1952 to 2007). 
Comment briefly on the dominant features you see in the data.
As in Question 2, make sure your plots are labeled and easy to read, and put all the plots in one figure with a title.
Look at the seaborn [FacetGrid API reference](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
for ideas.

### Visualization result

![TE of LE by conti](https://user-images.githubusercontent.com/45035308/192679111-4d7a0ab7-b779-4126-a339-9c20d1b72133.png)


## Question 3 -- life expectancy vs GDP

Use scatter plots to visualize the relationship between life expectancy and GDP per capita. 
Compare the use of linear and log scales for GDP. Comment on the relationships that seem significant and any outliers you notice.

### Visualization result

![LE vs GDP](https://user-images.githubusercontent.com/45035308/192679191-df3f3ed6-20d3-4f8d-b059-a2681c3ddb0f.png)


## Question 4 -- PDF of life expectancy

* Overlay the normal (Gaussian) distribution on a normalized version of the histogram for the entire dataset.
* Include the KDE, which is discussed here: [Kernel Density Estimation](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation) -- pydata.org
* From ISLR2 p156: kernel density estimator is essentially a smoothed version of a histogram
* Consider using [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) -- scipy.org
* Comment briefly on the result (i.e., explain the dominant features in the chart with a few sentences).
  * Make sure to use the results in previous questions to justify your interpretation.

### Visualization result

![Pdf of LE](https://user-images.githubusercontent.com/45035308/194662126-90190c26-8ab7-4ccd-9037-0254b26184cb.png)



## Instructions for reproducing these results

* Download the tsv data file(gapminder.tsv)
* Create a new py or ipynb file(referring to hw1_gapminder.ipynb)
* This contains import required libraries and reads the tsv file using pandas and loads the dataset
* Run subsequent cells each corresponding to a question asked above, and gets executed producing the results


