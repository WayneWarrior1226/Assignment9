## BEGIN Work ticket 4 Veronica Dean (3/24/2022) here

#Import packages to read csv file and write a new json file
import csv, json

csvFilePath= 'SalesJan2009.csv'
jsonFilePath = 'Salesjan2009.json'
fieldnames = ("Transaction_date","Product","Price","Payment_Type","Name","Ciy","State","Country")

reader = csv.DictReader( csvFilePath, fieldnames)
for row in reader:
    json.dump(row, jsonFilePath)
    jsonFilePath.write('\n')

## END Work ticket 4 Veronica Dean (3/24/2022) here
## HALF-LIFE /  Bass / John Richards Sr. / After-Burner Elite 
