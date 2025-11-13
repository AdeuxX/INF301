import csv
from execution_time import mesure_time

file_name = 'dataset'

@mesure_time
def load_data(file_name):
    with open(f"{file_name}.csv","r") as file:
        file_csv = csv.reader(file)
        datas = []
        for row in file_csv:
            datas.append(row)
    return datas
print(load_data(file_name))