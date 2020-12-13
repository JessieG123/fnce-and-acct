import unittest
from src import solvency as ratios

class ratiosTest(unittest.TestCase):
    def debtToTotalAssets(self):
        self.assertEqual(ratios.debtToTotalAssets(1000, 20), 50)

    def timesInterestEarned(self):
        self.assertEqual(ratios.timesInterestEarned(5000, 10), 500)

    def freeCashFlow(self):
        self.assertEqual(ratios.freeCashFlow(1000, 300, 500), 2.5)

if __name__ == '__main__':
    unittest.main()
