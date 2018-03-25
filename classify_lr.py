''' Logistic Regression '''
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

from csv_handler import load_csv

def lr(file_name, predict_me):
    ''' Logistic Regression Module '''
    # # load the datasets
    trainer, target = load_csv(file_name)

    # # fit a logistic regression model to the data
    model = LogisticRegression()
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
# lr(FILE_NAME)
