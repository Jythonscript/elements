#!/usr/bin/env python3
class Element:
    def __init__(self, s, n, a):
        self.symbol = s
        self.name = n
        self.anum = a

    def getSymbol(self):
        return self.symbol

    def getName(self):
        return self.name

    def getAnum(self):
        return self.anum

    def toString(self):
        return str(self.anum) + "\t" + self.name + "\t(" + self.symbol + ")"
