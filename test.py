import numpy
import scipy
from numpy import log,sqrt,exp
from scipy.stats import norm
class BlackScholesModel:
    def __init__(self,
        timeToMaturity,
        riskFreeRate,
        volatility,
        currentPrice,
        strikePrice
    ):
        self.timeToMaturity = timeToMaturity
        self.strikePrice = strikePrice
        self.currentPrice = currentPrice
        self.riskFreeRate = riskFreeRate
        self.volatility = volatility
    def calculate(self):
        first = norm.cdf(self.d1())*self.currentPrice
        second = norm.cdf(self.d2())*self.strikePrice*exp(-self.riskFreeRate*self.timeToMaturity)
        return (first-second)
        
    def d1(self):
        numerator = log(self.currentPrice/self.strikePrice)+(self.riskFreeRate+(self.volatility**2)/2)*self.timeToMaturity
        denominator = self.volatility*sqrt(self.timeToMaturity)
        return numerator/denominator
    def d2(self):
        return self.d1()-self.volatility*sqrt(self.timeToMaturity)
B = BlackScholesModel(1,100,100,0.2,0.05)
print(B.calculate())
