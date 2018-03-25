import csv
import numpy as np

def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    # print (dataset)
    trainer = []
    target = []

    for i in range(len(dataset)):
        # print (dataset[i])
        trainer.append([float(dataset[i][j]) for j in range(len(dataset[i])-1)])
        # print (dataset[i][16])
        target.append(dataset[i][16])

    return trainer, target

# filename = "temp.csv"
# trainer, target = load_csv(filename)
# print ("TRAINER", trainer)
# print ("TARGET", target)
# print ("Loaded data file {0} with {1} rows :", filename, "-", len(target))