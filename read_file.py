import csv

with open('ratings.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(row[0].split(","))
        # print(', '.join(row))