import csv
with open('GLdetail.txt', 'r') as FileIn, open('GLdetailfix.txt', 'w', newline='') as FileOut:
    writer = csv.writer(FileOut)
    for row in csv.reader(FileIn):
        if (
			#excludes blank rows
			any(row)
			):
            writer.writerow(row)