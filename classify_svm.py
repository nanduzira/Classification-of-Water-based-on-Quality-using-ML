''' Support Vector Machine '''
from sklearn import metrics
from sklearn.svm import SVC

from csv_handler import load_csv

def svc(file_name, predict_me):
    ''' SVC Module '''
    # # load the datasets
    trainer, target = load_csv(file_name)

    # # fit a SVM model to the data
    model = SVC()
    model.fit(trainer, target)
    # print(model)

    # # make predictions
    expected = target
    predicted = model.predict(predict_me)
    # print(predicted)

    # # summarize the fit of the model
    # print(metrics.classification_report(expected, predicted))
    # print(metrics.confusion_matrix(expected, predicted))

    return predicted

# # Unit Test Part
# FILE_NAME = "temp.csv"
# svc(FILE_NAME)
