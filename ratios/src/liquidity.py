import common
"""
Liquidity ratios
"""
def workingCaptial(currentAssets, currentLiabilities):
    return currentAssets - currentLiabilities

def currentRatio(currentAssets, currentLiabilities):
    return currentAssets / currentLiabilities

def receivablesTurnover(creditSales, grossAcctReceivable1, grossAcctReceivable2):
    return creditSales / common.average(grossAcctReceivable1, grossAcctReceivable2)

def averageCollectionPeriod(creditSales, grossAcctReceivable1, grossAcctReceivable2):
    return 365 / receivablesTurnover(creditSales, grossAcctReceivable1, grossAcctReceivable2)

def inventoryTurnover(Cogs, inventory1, inventory2):
    return Cogs / common.average(inventory1, inventory2)

def daysInInventory(Cogs, inventory1, inventory2):
    return 365 / inventoryTurnover(Cogs, inventory1, inventory2)
