from TheAPI import RiotAPI
import LeagueRanks as lr
import time
import pKey as pKey
import csv
import math

api = RiotAPI(pKey.pkey)
numb_of_cols = [5,8,11,14] # Number for how many players are in CSV
poss_cols = [2,4,7,10,13] # Number for column of summoner name

def readCSV():
    cur_col = 1
    cur_row = 1
    count = 0
    filename = raw_input('Enter the csv files name. (Without .csv)')
    
    with open(filename+'.csv','rb') as f:
        reader = csv.reader(f)
        num_cols = len(next(reader))
        print(num_cols)
        theDict = [None] * int(math.ceil(float(num_cols)/float(3))) # I'm sure theres a way to make this look nicer
        for row in reader:
            if(cur_row == 1):
                for col in row:
                    print(col)
                    if(num_cols in numb_of_cols):
                        if(cur_col in poss_cols):
                            theDict[count] = col
                            cur_col += 1
                            count += 1
                        else:
                            cur_col += 1
                    else:
                        print("Format error")
                cur_row += 1
    return theDict

def getRank():
	names = readCSV() # Retrieve dictionary of names
	points = lr.divisionPoints
	theStuff = {}
	for name, val in (enumerate(names)):
		idd = api.get_summoner_by_name(names[name])
		theId = idd[val]['id']
		mm = str(theId)
		try:
			tier = api.get_rank(theId)[mm][0]['tier']
			div = api.get_rank(theId)[mm][0]['entries'][0]['division']
		except ValueError:
			tier = 'UNRANKED'
			div = ''
		theStuff[val] = tier + div
		time.sleep(4)
	return theStuff

def writeCSV():
    myDict = getRank()
    writer = csv.writer(open('output.csv','wb'))
    writer.writerow(myDict.keys())
    writer.writerow(myDict.values())
    

def main():
    writeCSV()

if __name__ == "__main__":
    main()
