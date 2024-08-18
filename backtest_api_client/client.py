import requests

class BacktestAPIClient:
    def __init__(self, base_url='http://68.183.83.98:8000'):
        self.base_url = base_url

    def get_equity_data(self, symbol, start_date, end_date, interval='min'):
        """
        Fetches equity data from the API.

        :param symbol: The symbol for which data is requested.
        :param start_datet: The start date in 'YYYY-MM-DD' format.
        :param end_datet: The end date in 'YYYY-MM-DD' format.
        :param interval: The data interval ('min' for minute-level, 'D' for daily).
        :return: The JSON response from the API.
        """
        url = f"{self.base_url}/getEquityData"
        params = {
            'symbol': symbol,
            'startDate': start_date,
            'endDate': end_date,
            'interval': interval
        }
        response = requests.get(url, params=params)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        return response.json()
