import numpy as np
import pandas as pd
import graphviz 
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

tennis = pd.read_csv('./tp6-csp/code/id3/tennis.csv')
Le = LabelEncoder()

tennis['outlook'] = Le.fit_transform(tennis['outlook'])
tennis['temp'] = Le.fit_transform(tennis['temp'])
tennis['humidity'] = Le.fit_transform(tennis['humidity'])
tennis['windy'] = Le.fit_transform(tennis['windy'])
tennis['play'] = Le.fit_transform(tennis['play'])

y = tennis['play']
X = tennis.drop(['play'],axis=1)

clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, y)

print(tree.plot_tree(clf))

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("tennis")

X_pred = clf.predict(X)
print(X_pred==y)