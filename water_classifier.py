''' Compare the Confidence for Various Classifers '''
from statistics import mode

from classify_dtc import dtc
from classify_knn import knn
from classify_lr import lr
from classify_nb import nb
from classify_svm import svc

def classify_water(file_name, predict_me):
    ''' Classify the given water '''
    # # Call the Classification Algorithms
    dtc_prediction = dtc(file_name, predict_me)
    knn_prediction = knn(file_name, predict_me)
    lr_prediction = lr(file_name, predict_me)
    nb_prediction = nb(file_name, predict_me)
    svc_prediction = svc(file_name, predict_me)

    final_prediction = []
    
    # # Majority Result from thr Prediction Results
    for i in range(len(dtc_prediction)):
        class_type = 0
        temp_list = [dtc_prediction[i], knn_prediction[i], lr_prediction[i], nb_prediction[i], svc_prediction[i]]
        # print(temp_list)
        final_prediction.append(mode(temp_list))

    return final_prediction
   
# # Unit Test Part
# FILE_NAME = "temp.csv"
# PREDICT_ME = [[2.4, 482.0, 7.1, 371.1, 16.0, 166.0, 178.0, 43.3, 17.0, 34.0, 0.4, 0.56, 1.1, 13.4, 1100.0, 11.26086957],
#             [2.3, 1335.0, 6.9, 1027.9, 26.0, 142.0, 418.0, 117.7, 30.1, 306.0, 0.5, 0.52, 3.8, 55.4, 240.0, 0.0],
#             [0.1, 98.4, 6.1, 75.8, 16.0, 30.0, 22.0, 5.6, 1.9, 16.0, 0.12, 0.25, 3.3, 3.2, 240.0, 11.26086957],
#             [1.9, 469.0, 6.9, 361.1, 18.0, 104.0, 90.0, 24.8, 6.8, 56.0, 0.1, 0.36, 3.9, 41.6, 95.0, 11.26086957],
#             [0.1, 269.0, 5.9, 207.1, 58.0, 56.0, 54.0, 13.6, 4.9, 42.0, 0.2, 0.14, 15.6, 10.5, 240.0, 11.26086957],
#             [50.1, 259.0, 6.4, 199.4, 30.0, 84.0, 60.0, 16.8, 4.4, 20.0, 0.4, 2.9, 2.3, 9.5, 240.0, 0.0],
#             [0.3, 242.0, 6.5, 186.3, 20.0, 26.0, 70.0, 18.4, 5.8, 24.0, 0.11, 0.11, 1.3, 11.4, 23.0, 0.0],
#             [6.5, 892.0, 7.1, 686.8, 20.0, 168.0, 278.0, 79.3, 19.4, 18.0, 0.16, 1.4, 7.6, 417.6, 1100.0, 9.0],
#             [0.2, 387.0, 6.5, 297.9, 16.0, 90.0, 92.0, 23.2, 8.3, 50.0, 0.18, 0.04, 12.4, 23.7, 1100.0, 11.26086957],
#             [33.2, 49.2, 5.6, 37.9, 24.0, 6.0, 16.0, 3.2, 1.9, 12.0, 0.36, 3.9, 2.5, 1.2, 240.0, 0.0],
#             [0.3, 42.6, 5.8, 32.8, 8.0, 12.0, 10.0, 2.4, 0.97, 16.0, 0.3, 0.08, 0.4, 1.8, 240.0, 11.26086957],
#             [0.1, 613.0, 6.8, 472.0, 20.0, 98.0, 206.0, 67.2, 9.2, 56.0, 0.4, 0.1, 14.9, 19.2, 240.0, 11.26086957],
#             [1.0, 85.1, 6.2, 65.6, 12.0, 24.0, 22.0, 7.2, 1.5, 30.0, 0.31, 0.29, 1.8, 1.5, 1100.0, 0.0],
#             [0.3, 164.0, 5.9, 126.3, 28.0, 32.0, 40.0, 11.2, 2.9, 32.0, 0.3, 0.0, 13.4, 4.6, 1100.0, 11.26086957],
#             [0.4, 242.0, 7.4, 186.3, 22.0, 60.0, 64.0, 19.2, 3.89, 34.0, 0.19, 0.03, 3.8, 9.8, 240.0, 0.0],
#             [0.7, 974.0, 5.8, 749.9, 9.0, 38.0, 108.0, 25.6, 10.6, 44.0, 0.49, 0.28, 16.8, 37.4, 1100.0, 11.26086957],
#             [0.1, 328.0, 6.1, 252.6, 36.0, 44.0, 70.0, 19.2, 5.3, 20.0, 0.1, 0.0, 2.5, 35.8, 1100.0, 11.26086957],
#             [0.1, 328.0, 6.1, 252.6, 36.0, 44.0, 70.0, 19.2, 5.3, 20.0, 0.1, 0.0, 2.5, 35.8, 1100.0, 11.26086957]]
# print(classify_water(FILE_NAME, PREDICT_ME))
