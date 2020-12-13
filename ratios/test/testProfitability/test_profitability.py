import unittest
from src import profitability as ratios

class ratiosTest(unittest.TestCase):
    def test_grossProfitMargin(self):
        self.assertEqual(ratios.grossProfitMargin(1000, 20), 50)

    def test_profitMargin(self):
        self.assertEqual(ratios.profitMargin(5000, 10), 500)

    def test_assetTurnover(self):
        self.assertEqual(ratios.assetTurnover(1000, 300, 500), 2.5)

    def test_returnOnAssets(self):
        self.assertEqual(ratios.returnOnAssets(2030, 200, 700), 2030/450)

    def test_returnOnShe(self):
        self.assertEqual(ratios.returnOnShe(4000, 35, 100, 200), 3965/150)

    def test_basicEarningsPerShare(self):
        self.assertEqual(ratios.basicEarningsPerShare(6000, 40, 100), 59.6)

    def test_priceEarningsRatio(self):
        self.assertEqual(ratios.priceEarningsRatio(600, 6000, 40, 100), 600/59.6)

    def test_payoutRatio(self):
        self.assertEqual(ratios.payoutRatio(50, 2000), 0.025)

    def test_dividendYield(self):
        self.assertEqual(ratios.dividendYield(10, 60), 1/6)

if __name__ == '__main__':
    unittest.main()
