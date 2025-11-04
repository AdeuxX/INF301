import csv
file_name = 'dataset'
with open(f"{file_name}.csv","r") as file:
    file_csv = csv.reader(file)
    datas = []
    for row in file_csv:
        datas.append(row)
print(datas)