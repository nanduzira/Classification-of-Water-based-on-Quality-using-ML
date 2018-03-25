''' CSV File Handler '''
import csv

def load_csv(file_name):
    ''' Load a Basic CSV File '''
    # # Retrieve Data as a List
    lines = csv.reader(open(file_name, "r"))
    dataset = list(lines)
    
    # # Intialize Trainer & Target Lists
    trainer = []
    target = []

    # # Seperate the Trainer & Target from the List
    for i in range(len(dataset)):
        trainer.append([float(dataset[i][j]) for j in range(len(dataset[i])-1)])
        target.append(dataset[i][16])

    return trainer, target

# # Unit Test Part
# FILE_NAME = "temp.csv"
# TRAINER, TARGET = load_csv(FILE_NAME)
# print("TRAINER", TRAINER)
# print("TARGET", TARGET)
# print("Loaded data file {0} with {1} rows :", FILE_NAME, "-", len(TARGET))
