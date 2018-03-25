# Gaussian Naive Bayes
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

from csv_handler import load_csv
import numpy as np

filename = "temp.csv"
trainer, target = load_csv(filename)

# print (trainer, "\n", target)

# load the datasets
dataset = datasets.load_iris()
# print (dataset.target)
# print (type(dataset.data[]))

# # fit a Naive Bayes model to the data
model = GaussianNB()
model.fit(trainer, target)
print(model)

# # make predictions
expected = target
# test = np.asarray([0.2, 350.0, 3.9, 269.5, 100.0, 16.0, 86.0, 20.8, 8.3, 36.0, 0.09, 0.16, 9.975805169, 8.9, 1.0, 0.0])
# test.reshape(1, -1)
# print (test)
predicted = model.predict([[0.2, 350.0, 3.9, 269.5, 100.0, 16.0, 86.0, 20.8, 8.3, 36.0, 0.09, 0.16, 9.975805169, 8.9, 1.0, 0.0]])
print (predicted)
# print (type(dataset.target))
# print (type(np.asarray([0.2, 350.0, 3.9, 269.5, 100.0, 16.0, 86.0, 20.8, 8.3, 36.0, 0.09, 0.16, 9.975805169, 8.9, 1.0, 0.0])))

# summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))
