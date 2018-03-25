''' Gaussian Naive Bayes '''
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

from csv_handler import load_csv

def nb(file_name, predict_me):
    ''' Naive Bayes Module '''
    # # load the datasets
    trainer, target = load_csv(file_name)

    # # fit a Naive Bayes model to the data
    model = GaussianNB()
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
# nb(FILE_NAME)
