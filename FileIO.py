import csv

def readfile(filename):
# Opens and closes File
    with open("FullDataFor20241.csv", "r", encoding='cp1252') as csvFile:
        reader = csv.DictReader(csvFile)



readfile("FullDataFor20241.csv")
