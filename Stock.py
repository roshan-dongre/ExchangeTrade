#Stock class to handle the specific information for each unique symbol
class Stock(object):
    
    #initialize the instance variables you will need
    def __init__(self, timestamp, symbol, quantity, price):
        self.timestamp = int(timestamp)
        self.symbol = symbol
        self.quantity = int(quantity)
        self.price = int(price)
        self.totalvolprice = int(price)*int(quantity)
        self.maxtime = 0
    
    #check if you are dealing with the same symbol
    def nameEqual(self,othersymbol):
        if(self.symbol==othersymbol.symbol):
            return True
        return False
    
    #update the volume of the original
    def addVolume(self,othersymbol):
        self.quantity+=othersymbol.quantity
    
    #update the price*volume to make the wieghted average faster to find
    def priceTimesVolume(self,othersymbol):
        self.totalvolprice+=othersymbol.totalvolprice
    
    #keep checking if you have the max price for the symbol
    def maxPrice(self,othersymbol):
        if (self.price<othersymbol.price):
            self.price = othersymbol.price
    
    #find the weighted average once you have the total volume and vol*price
    def findWeightedAverage(self):
        return(self.totalvolprice/self.quantity)
    
    #since its consecutive you just need to check with the last time recorded
    #so keep updating the timestamp to keep moving forward
    def findTimeStampDiff(self, othersymbol):
        if (othersymbol.timestamp-self.timestamp>self.maxtime):
            self.maxtime = othersymbol.timestamp-self.timestamp
        self.timestamp = othersymbol.timestamp