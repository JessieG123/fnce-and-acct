
def average(value1, value2):
    return (value1 + value2)/2
"""
Profitablity ratios
"""
#calculates gross profit margin 
def grossProfitMargin(grossProfit, sales):
    return grossProfit/sales

def profitMargin(netIncome, sales):
    return netIncome/sales

def assetTurnover(sales, currentAssets, prevAssets):
    return sales/average(currentAssets, prevAssets)

def returnOnAssets(netIncome, currentAssets, prevAssets):
    return netIncome/average(currentAssets, prevAssets)

def returnOnShe(netIncome, dividends, currentShe, prevShe):
    return (netIncome - dividends)/average(currentShe, prevShe)

def basicEarningsPerShare(netIncome, dividends, weightedAvgCommonShares):
    return (netIncome - dividends)/weightedAvgCommonShares

def priceEarningsRatio(marketPricePerShare, netIncome, dividends, weightedAvgCommonShares):
    return marketPricePerShare/basicEarningsPerShare(netIncome, dividends, weightedAvgCommonShares)

def payoutRatio(cashDividendDeclared, netIncome):
    return cashDividendDeclared/netIncome

def dividendYield(dividendDeclaredPerShare, marketPricePerShare):
    return dividendDeclaredPerShare/marketPricePerShare
