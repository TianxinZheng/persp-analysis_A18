class Stock_Info(object):
    def __init__(self, date, ticker, opening_price, closing_price):
        self._date = date
        self._ticker = ticker
        self._opening_price = opening_price
        self._closing_price = closing_price

    @property
    def date(self):
        return self._date

    @property
    def ticker(self):
        return self._ticker

    @property
    def opening_price(self):
        return self._opening_price

    @property
    def closing_price(self):
        return self._closing_price

    @closing_price.setter
    def closing_price(self, correct_value):
        self._closing_price = correct_value

    def __repr__(self):
        return "|".join([self.date, self.ticker, 
                         self.opening_price, self.closing_price])



def create_dict(data):
    rv = {}
    for row in data:
        tkr = row[TICKER]
        s = Stock_Info(row[DATE], tkr, row[OPEN], row[CLOSE])
        if tkr not in rv:
            rv[tkr] = []
        rv[tkr].append(s)

    return rv
        

def mystery(d, list0):
    for (x, y, z) in list0:
        for a in d[x]:
            if a.date == y:
                a.closing_price = z
                break


d = create_dict(stocks)
entries = [["GOOG", '2010-11-09', '625.00'], 
           ['GOOG', '2010-11-10', '634.82']]
mystery(d, entries)
for s in d["GOOG"]:
    print(s)