import Stock
import csv

def readFile():
    #list containing each unique symbol
    stocklist = []
    filename = 'input.csv' #CHANGE THIS FOR A DIFFERENT FILE
    #opens the file without reading entire thing into memory
    with open(filename) as csvfile: 
        #add fieldnames for easier access
        reader = csv.DictReader(csvfile, fieldnames=['timestamp','symbol','quantity','price'])
        #iterate throw the input file        
        for row in reader:
             stocktemp = Stock.Stock(row['timestamp'],row['symbol'],row['quantity'],row['price'])
             #length check included to make sure you can add the first stock in
             if(len(stocklist) != 0): 
                 #counter included to make sure you dont keep repeating symbols
                 counter = 0
                 #if you have seen this symbol already call the methods in the stock class and update
                 for stock in stocklist:
                     if(stocktemp.nameEqual(stock)):
                         counter+=1
                         stock.addVolume(stocktemp)
                         stock.priceTimesVolume(stocktemp)
                         stock.maxPrice(stocktemp)
                         stock.findTimeStampDiff(stocktemp)
                 #you havnt seen this symbol yet so add it into the list
                 if(counter == 0):
                     stocklist.append(stocktemp)
             else:
                stocklist.append(stocktemp)
    #sort the list in ascending order based on the symbol
    stocklist.sort(key = lambda stock: stock.symbol, reverse = False)
    writeFile(stocklist)

def writeFile(stocklist):
    #Open up a new file to write into that is csv based
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL, dialect = 'excel')
        #write in the values in the specified order        
        for value in stocklist:
            writer.writerow((value.symbol, value.maxtime, value.quantity, int(value.findWeightedAverage()), value.price))

readFile()
