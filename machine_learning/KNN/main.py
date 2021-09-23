import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from sklearn import linear_model, preprocessing
import sklearn

data = pd.read_csv("E:\projects\AI\machine_learning\KNN\car.data")

print(data.head())


le = preprocessing.LabelEncoder()

buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safty = le.fit_transform(list(data["safty"]))
cls = le.fit_transform(list(data["class"]))


X = list(zip(buying, maint, door, persons, lug_boot, safty))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

print(y_train[:10])