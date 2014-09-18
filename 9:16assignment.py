import cvs, string

reader = cvs.reader(open("blsdata.csv", rU), dialect = csv.excel)

reader.next()

unemployment-list = []



for row in reader:
	unemployment-list.append(row)
	
for index, obj in enumerate(unemployment-list):


		
	
print "The Labor Department reported on Sept. 5 that the unemployment rate dropped to %s percent in Aug. That's down 1.1 percentage points campared to %s percent in Aug. 2013." % ()
	
	