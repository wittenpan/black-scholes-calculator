import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    def __init__(self, time_to_maturity, risk_free_rate, volatility, current_price, strike_price):
        self.time_to_maturity = float(time_to_maturity)
        self.strike_price = float(strike_price)
        self.current_price = float(current_price)
        self.risk_free_rate = float(risk_free_rate)
        self.volatility = float(volatility)

    def calculate(self):
        try:
            first = norm.cdf(self.d1()) * self.current_price
            second = norm.cdf(self.d2()) * self.strike_price * np.exp(-self.risk_free_rate * self.time_to_maturity)
            return round(first - second, 4)
        except:
            return None

    def d1(self):
        numerator = (np.log(self.current_price/self.strike_price) + 
                    (self.risk_free_rate + (self.volatility**2)/2) * self.time_to_maturity)
        denominator = self.volatility * np.sqrt(self.time_to_maturity)
        return numerator/denominator

    def d2(self):
        return self.d1() - self.volatility * np.sqrt(self.time_to_maturity) 