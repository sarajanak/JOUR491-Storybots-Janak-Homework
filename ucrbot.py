import csv, string, datetime

reader = csv.reader(open("ucrdata.csv", "rU"), dialect = csv.excel)

reader.next()

for row in reader:
    try:
        violentrate12 = (float(row[4])/float(row[3]))*100000
        violentrate11 = (float(row[15])/float(row[14]))*100000
        violentrate10 = (float(row[25])/float(row[24]))*100000
        
        if violentrate12 > violentrate11:
        	phrase = "went up"
        elif violentrate12 < violentrate11:
        	phrase = "went down"
        else:
        	phrase = "held steady"
        	
        if violentrate12 > violentrate11 > violentrate10:
        	conditionalphrase = ", the third year in a row the rate has gone up"
        elif violentrate12 < violentrate11 < violentrate10:
        	conditionalphrase = ", the third year in a row the rate has gone down"
        else:
        	conditionalphrase = ""
    except:
        continue
    
    print "The violent crime rate in %s, %s %s from 2012 to 2011%s, with the rate now standing at %.2f per 100,000 people." % (row[2], row[1], phrase, conditionalphrase, violentrate12)



