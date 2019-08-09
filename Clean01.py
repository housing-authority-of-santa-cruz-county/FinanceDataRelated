import csv
with open('GLdetail02.csv', 'r') as FileIn, open('GLdetail02ETL.csv', 'w', newline='') as FileOut:
    writer = csv.writer(FileOut)
    for row in csv.reader(FileIn):
        if (
			#excludes blank rows
			any(row) and
			#excludes page header rows
			row[0] != "Run By:" and 
			row[15] != "Detailed General Ledger" and 
			row[13] != "From  July 2016 to December 2018" and
			row[3] != "Code" and
			#excludes page footer rows
			not row[0].startswith("Date")
			):
            writer.writerow(row)