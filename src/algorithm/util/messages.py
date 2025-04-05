from types import OrderSide

class MarketData:
    def __init__(
            self,
            time: int,
            o: float,
            h: float,
            l: float,
            c: float,
            v: float,
            vwap: float
    ):
        self.time = time
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.v = v
        self.vwap = vwap

class FnGData:
    def __init__(self):
        pass

class gtrendsData:
    def __init__(self):
        pass

class finbertData:
    def __init__(self):
        pass