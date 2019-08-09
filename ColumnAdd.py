import csv
with open('GLdetail02ETL.csv','r') as csvinput:
    with open('GLdetail02ETL2.csv', 'w',newline='') as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            writer.writerow(row+['Berry'])