import csv
 
in_file = 'GLdetailFix.txt' # change this accordingly
out_file = 'GLdetailFix.csv'
with open(in_file, 'r') as in_f, open(out_file, 'w', newline='') as out_f:
	rdr =  csv.DictReader(in_f)
	rdr.fieldnames[0]='Date'
	rdr.fieldnames[1] = 'F2'
	rdr.fieldnames[2] = 'F3'
	rdr.fieldnames[3] = 'Journal'
	rdr.fieldnames[4] = 'F5'
	rdr.fieldnames[5] = 'Code'
	rdr.fieldnames[6] = 'F7'
	rdr.fieldnames[7] = 'F8'
	rdr.fieldnames[8] = 'BatchID'
	rdr.fieldnames[9] = 'F10'
	rdr.fieldnames[10] = 'F11'
	rdr.fieldnames[11] = 'F12'
	rdr.fieldnames[12] = 'Description'
	rdr.fieldnames[13] = 'F14'
	rdr.fieldnames[14] = 'F15'
	rdr.fieldnames[15] = 'F16'
	rdr.fieldnames[16] = 'F17'
	rdr.fieldnames[17] = 'F18'
	rdr.fieldnames[18] = 'F19'
	rdr.fieldnames[19] = 'Amount'
	rdr.fieldnames[20] = 'F20'
	rdr.fieldnames[21] = 'F21'
	rdr.fieldnames[22] = 'F22'
	rdr.fieldnames[23] = 'F23'
	# Insert new columns
	fieldnames =  ['Fund', 'FundDesc','Status','Account','Project','LineItem','LineItemDesc','Period']
	fieldnames.extend(rdr.fieldnames)

	wrtr = csv.DictWriter(out_f, fieldnames=fieldnames)
	wrtr.writeheader()
	FundValue=''
	FundDescValue=''
	StatusValue=''
	LineItemValue=''
	LineItemDescValue=''
	AccountValue=''
	ProjectValue=''
	PeriodValue=''
	for row_id, row in enumerate(rdr):
		if row[:4]=='Date'Skip=True
		if row[:4]=='F1=
		# Capture Fund
		if row['Date']=='Fund':
			FundValue=row['F2']
			FundDescValue=row['F7']
			StatusValue=row['F18']
		# Capture LineItem
		if row['F5'] !='':
			LineItemValue = row['F5']
			LineItemDescValue = row['F11']
			AccountValue = LineItemValue.split('.')[1]
			ProjectValue = LineItemValue.split('.')[2]
		# Capture Period
		if row['F19'] =='Period:':
			PeriodValue= row['Amount']
		# Set values of new columns
		row['Fund'] = FundValue
		row['FundDesc'] = FundDescValue
		row['Status'] = StatusValue
		row['Account'] = AccountValue
		row['Project'] = ProjectValue
		row['LineItem'] = LineItemValue
		row['LineItemDesc'] = LineItemDescValue
		row['Period'] = PeriodValue
		# Write row into File Output
		wrtr.writerow(row)