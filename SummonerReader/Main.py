#from BalancerAPI import RiotAPI
#import BalancerRanks as bb
import time
import pKey as pKey
import csv
#api = RiotAPI(pKey.api_key)

def readCSV():
    theDict = {}
    cur_col = 1
    cur_row = 0
    count = 0
    filename = raw_input('Enter the csv files name. (Without .csv)')
    
    with open(filename+'.csv','rb') as f:
        reader = csv.reader(f,delimiter='\t')
        num_cols = len(next(reader))
        for row in reader:
            print(row)
            if(cur_row == 1):
                for col in row:
                    print(col)
                    if(num_cols == 5):
                        if(cur_col == 2):
                            theDict[col] = col
                            count += 1
                        elif(cur_col == 4):
                            theDict[col] = count
                            count += 1
                        cur_col += 1
                    elif(num_cols == 8):
                        if(cur_col == 2):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 4):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 7):
                            theDict[col] = count
                            count += 1
                        cur_col += 1
                    elif(num_cols == 11):
                        if(cur_col == 2):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 4):
                            theDict[col] = count
                            count += 1
                        elif(cur_coll == 7):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 10):
                            theDict[col] = count
                            count += 1
                        cur_col += 1
                    elif(num_cols == 14):
                        if(cur_col == 2):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 4):
                            theDict[col] = count
                            count += 1
                        elif(cur_coll == 7):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 10):
                            theDict[col] = count
                            count += 1
                        elif(cur_col == 13):
                            theDict[col] = count
                            count += 1
                        cur_col += 1
            else:
                cur_row += 1
    return theDict

def main():
    new = readCSV()
    print new

if __name__ == "__main__":
    main()
