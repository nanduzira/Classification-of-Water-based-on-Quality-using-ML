# # k-Nearest Neighbor
from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

from csv_handler import load_csv

# # K Neighbors Classifier Module
def knn(filename):
    # # load the datasets
    trainer, target = load_csv(filename)

    # # fit a k-nearest neighbor model to the data
    model = KNeighborsClassifier()
    model.fit(trainer, target)
    print(model)

    # # make predictions
    expected = target
    predicted = model.predict([[2.1, 137.6, 7.2, 1059.5, 38.0, 88.0, 180.0, 22.4, 30.0, 336.0, 0.38, 0.4, 9.975805169, 36.8, 1.0, 11.26086957], [0.2, 350.0, 3.9, 269.5, 100.0, 16.0, 86.0, 20.8, 8.3, 36.0, 0.09, 0.16, 9.975805169, 8.9, 1.0, 0.0]])
    print (predicted)

    # # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

filename = "temp.csv"
knn(filename)
