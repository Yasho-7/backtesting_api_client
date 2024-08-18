import unittest
from backtest_api_client import BacktestAPIClient

class TestBacktestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = BacktestAPIClient()

    def test_get_equity_data(self):
        response = self.client.get_equity_data('RELIANCE', '2022-01-01', '2023-01-02')
        # print(response)
        self.assertIsInstance(response, list)
        # Add more assertions based on expected response

if __name__ == '__main__':
    unittest.main()
