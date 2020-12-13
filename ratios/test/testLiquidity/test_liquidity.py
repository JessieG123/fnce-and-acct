import unittest
from src import liquidity as ratios

class ratiosTest(unittest.TestCase):
    def workingCaptial(self):
        self.assertEqual(ratios.workingCaptial(1000, 20), 50)

    def currentRatio(self):
        self.assertEqual(ratios.currentRatio(5000, 10), 500)

    def receivablesTurnover(self):
        self.assertEqual(ratios.receivablesTurnover(1000, 300, 500), 2.5)

    def averageCollectionPeriod(self):
        self.assertEqual(ratios.averageCollectionPeriod(2030, 200, 700), 2030/450)

    def inventoryTurnover(self):
        self.assertEqual(ratios.inventoryTurnover(4000, 35, 100, 200), 3965/150)

    def daysInInventory(self):
        self.assertEqual(ratios.daysInInventory(6000, 40, 100), 59.6)

if __name__ == '__main__':
    unittest.main()
