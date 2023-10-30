import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from decisionTreeClassifier import DecisionTreeClassifier

col_names = ["outlook", "temp", "humidity", "windy", "play"]
data = pd.read_csv("./tp7-ml/code/id3/tennis.csv", skiprows=1,header=None, names=col_names)
print(data.head(10))

X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values.reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
classifier.fit(X_train, Y_train)
classifier.print_tree()

Y_pred = classifier.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, Y_pred))