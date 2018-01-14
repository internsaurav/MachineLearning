import numpy as np
import pandas as pd
import xlrd
import re

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# import module to calculate model perfomance metrics
from sklearn import metrics

#year - years for which data is being analyzed
def main():
	output = ""
	year,food_production_data = extract_production_data("food_production_data.xlsx")
	food_import_data = extract_import_data("food_import_sources.xlsx")
	population_data = extract_population_data("population_data.txt")
	combined_data = makeDataFrame(year,food_production_data,population_data,food_import_data)
	output += "DataFrame:\n"
	output += str(combined_data)+"\n\n"
	coeff_of_determination,rmse,coefficients,y_test,y_pred,intercept = apply_linear_regression(combined_data)
	output += "y_test:\n"+str(y_test)+"\n\n"
	output += "y_predicted:\n"+str(y_pred)+"\n\n"
	output += "coeff_of_determination: " + str(coeff_of_determination) + "\n\n"
	output += "RMSE: " + str(rmse) + "\n\n"
	output += "Regression Equation:\nEstimated_imports = population*" + str(coefficients[0]) + " + production*" + str(coefficients[1]) + " + "+str(intercept) + "\n"

	f = open("output.txt",'w')
	f.write(output)
	f.close()

def extract_production_data(filename):
	food_production_wb = xlrd.open_workbook(filename)
	food_production_sheet = food_production_wb.sheet_by_name("Table1")
	year = []
	food_production = []
	for row in range (59,75):
		year.append(int(food_production_sheet.cell(row,0).value)) 
		food_production.append(food_production_sheet.cell(row,1).value)
	return year,food_production

def extract_import_data(filename):
	food_import_wb = xlrd.open_workbook(filename)
	food_import_sheet = food_import_wb.sheet_by_name("Sources")
	food_import = []
	for col in range (3,19):
		food_import.append(food_import_sheet.cell(70,col).value)
	return food_import

def extract_population_data(filename):
	population_file = open(filename,'r')
	population_data_raw = population_file.readlines()
	population_data = [float(re.split(r'\t+',x)[1].split()[0]) for x in population_data_raw]
	population_file.close()
	population_data.reverse()
	return population_data

def makeDataFrame(index,food_production_data,population_data,food_import_data):
	d = {"production":food_production_data, "population": population_data, "imports":food_import_data}
	combined_data = pd.DataFrame(d,index)
	import_data = combined_data.pop("imports")
	combined_data.insert(2,"imports",import_data)
	return combined_data

def apply_linear_regression(data):
	feature_names = ["population","production"]
	X = data[feature_names]
	y = data.imports
	linreg = LinearRegression()
	X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75,test_size=0.25, random_state=42)
	linreg.fit(X_train, y_train)
	coeff_of_determination = linreg.score(X_train, y_train)
	y_pred = linreg.predict(X_test)
	rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
	coefficients = linreg.coef_
	intercept =  linreg.intercept_
	return coeff_of_determination,rmse,coefficients,y_test,y_pred,intercept

if __name__ == '__main__':
	main()