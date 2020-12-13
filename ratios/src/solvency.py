
"""
Solvency ratios
"""

def debtToTotalAssets(totalLiabilities, totalAssets):
    return totalLiabilities / totalAssets

def timesInterestEarned(netIncome, interestExpense, ebit):
    return (netIncome + interestExpense + ebit) / interestExpense

def freeCashFlow(netCashOperatingActivies, netCaptialExpenditures, dividendsPaid):
    return netCashOperatingActivies - netCaptialExpenditures - dividendsPaid
