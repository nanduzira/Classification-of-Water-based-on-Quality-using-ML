import csv
import numpy as np

def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    print (dataset)

    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]

    return dataset

filename = "temp.csv"
dataset = load_csv(filename)
print (dataset)
print ("Loaded data file {0} with {1} rows :", filename, "-", len(dataset))