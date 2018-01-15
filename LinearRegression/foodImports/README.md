# Application of Linear Regression to find a re3lation between food imports, food procudtion and population
This code attempts to find a relation between US food production, its population and its food imports using linear regression.<br /><br />

Following are the sources of data:<ol>
	<li> Food production data file: https://www.ers.usda.gov/webdocs/DataFiles/47679/table01.xlsx?v=43018</li>
	<li> Population Data : http://www.multpl.com/united-states-population/table</li>
	<li> Food imports Data : https://www.ers.usda.gov/webdocs/DataFiles/53736/food_import_sources.xlsx?v=42093</li></ol>
The files are uploaded for reference.<br />

It is kind of intuitive that Food imports of a country should:<ol>
	<li>increase with its population. (directly proportional)</li>
	<li>decerase with increase in its own production. (inversely proportional)</li></ol>
Although there might be other factors that influence the food imports, we are considering this simple case and trying to see if linear regression can predict the value of food imports well enough.
We are analyzing the data for the period 1999-2014.

The output file is also uploaded. We can see that even with very less data, the results are fair. The coefficient of determination is pretty high (96%) which indicates that the regression line approximates the data points very well.
RMSE value is 8334 which is 7% is best case and 20% in worst case.
