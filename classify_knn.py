''' k-Nearest Neighbor '''
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

from csv_handler import load_csv

def knn(file_name, predict_me):
    ''' k-Nearest Neighbor Module '''
    # # load the datasets
    trainer, target = load_csv(file_name)

    # # fit a k-nearest neighbor model to the data
    model = KNeighborsClassifier()
    model.fit(trainer, target)
    print(model)

    # # make predictions
    expected = target
    predicted = model.predict(predict_me)
    print(predicted)

    # # summarize the fit of the model
    # print(metrics.classification_report(expected, predicted))
    # print(metrics.confusion_matrix(expected, predicted))

# # Unit Test Part
# FILE_NAME = "temp.csv"
# knn(FILE_NAME)
