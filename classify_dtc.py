''' Decision Tree Classifier '''
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

from csv_handler import load_csv

def dtc(file_name, predict_me):
    ''' Module for DTC operations '''
    # # load the datasets
    trainer, target = load_csv(file_name)

    # # fit a CART model to the data
    model = DecisionTreeClassifier()
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
# dtc(FILE_NAME)
