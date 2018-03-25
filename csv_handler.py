import csv
import numpy as np

def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    # print (dataset)

    # for i in range(len(dataset)):
    #     print (i)
    #     # dataset[i] = [float(x) for x in dataset[i]]
    
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            if dataset[i][j] == '':
                print ("NONE")

    array = np.asarray(dataset)
    print (type(array))

    return dataset

filename = "temp.csv"
dataset = load_csv(filename)
print ("Loaded data file {0} with {1} rows :", filename, "-", len(dataset))