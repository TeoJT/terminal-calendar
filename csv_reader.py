import csv

CSV_FILENAME = "save.csv"

def writeToCSV(row):
    file = open(CSV_FILENAME, "a")
    csvWriter = csv.DictWriter(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvWriter.writerow(row)
    file.close()

def readFromCSV():
    file = open(CSV_FILENAME, "r")
    csvReader = csv.DictReader(file)
    for row in csvReader:
        print(row)
    
        
def ensureNewline():
    with open(CSV_FILENAME, "r") as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
    if (last_line[-1] != '\n'):
        with open(CSV_FILENAME, "a") as f:
            f.write("")
    f.close()

        


readFromCSV()