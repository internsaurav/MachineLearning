import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz

def main():
	dataFile = "seeds_dataset.txt"
	data = pd.read_table(dataFile,delim_whitespace=True,header=None, names=('area' , 'perimeter' , 'compactness', 'kernel_len', 'kernel_wid', 'asymm_coef','k_groove_len','class'))
	y = data.pop('class') #We want to predict class
	X = data
	X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80,test_size=0.20, random_state=42)
	dtClassifier = tree.DecisionTreeClassifier()
	dtClassifier.fit(X_train,y_train)
	y_pred = dtClassifier.predict(X_test)
	score = dtClassifier.score(X_test,y_test)

	##Visualize the Tree
	dot_data = tree.export_graphviz(dtClassifier, out_file=None, feature_names=list(X),  
                         class_names=['Kama','Rosa','Canadian'],  
                         filled=True, rounded=True,  
                         special_characters=True)
	graph = graphviz.Source(dot_data)
	graph.render("Seeds")

	## Write Output
	output = "Test dataset:\n"+str(X_test)
	output += "\n\nPredicted value of target:\n" + str(y_pred)
	output += "\n\nActual value of target:\n" + str(y_test.values)
	output += "\n\nAccuracy: "+str(score)
	out = open("output.txt",'w+')
	out.write(output)
	out.close()
 
if __name__ == '__main__':
 	main()