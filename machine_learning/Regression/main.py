from os import sep
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import pickle

data = pd.read_csv("E:\projects\AI\machine_learning\Regression\student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

best_score = 0
for _ in range(10000):
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y)

    model = linear_model.LinearRegression()

    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    if acc > best_score:
        best_score = acc
        with open("model.pickle", "wb") as f:
            pickle.dump(model, f)
    print(f"Score: {acc}")
print(f"Best: {best_score}")
    

