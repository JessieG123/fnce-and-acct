import unittest
from src import ratios

class ratiosTest(unittest.TestCase):
    def test_grossProfitMargin(self):
        self.assertEqual(ratios.grossProfitMargin(1000, 20), 50)

    def test_profitMargin(self):
        self.assertEqual(ratios.profitMargin(5000, 10), 500)

    def test_assetTurnover(self):
        self.assertEqual(ratios.assetTurnover(1000, 20), 50)

    def test_returnOnAssets(self):
        self.assertEqual(ratios.returnOnAssets(1000, 20), 50)

    def test_returnOnShe(self):
        self.assertEqual(ratios.returnOnShe(1000, 20), 50)

    def test_basicEarningsPerShare(self):
        self.assertEqual(ratios.basicEarningsPerShare(1000, 20), 50)

    def test_priceEarningsRatio(self):
        self.assertEqual(ratios.priceEarningsRatio(1000, 20), 50)

    def test_payoutRatio(self):
        self.assertEqual(ratios.payoutRatio(1000, 20), 50)

    def test_dividendYield(self):
        self.assertEqual(ratios.dividendYield(1000, 20), 50)
if __name__ == '__main__':
    unittest.main()
