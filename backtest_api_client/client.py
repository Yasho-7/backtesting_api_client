import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

class BacktestAPIClient:
    def __init__(self, base_url='http://68.183.83.98:8000'):
        self.base_url = base_url
        self.chunk_size_days = 90  # Number of days per batch
        self.max_workers = 5  # Number of threads for parallel execution

    def fetch_data_chunk(self, url, params):
        """
        Fetches data for a single date range chunk from the API.

        :param url: The API endpoint URL.
        :param params: The parameters for the API request.
        :return: The JSON response from the API.
        """
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()

    def fetch_data_in_batches_parallel(self, url, params):
        """
        Fetches data from the API in batches and in parallel.

        :param url: The API endpoint URL.
        :param params: The parameters for the API request.
        :return: A combined list of results from all batches.
        """
        start_date = datetime.strptime(params['startDate'], '%Y-%m-%d')
        end_date = datetime.strptime(params['endDate'], '%Y-%m-%d')
        all_data = []

        # Prepare chunks of date ranges
        chunks = []
        while start_date < end_date:
            chunk_end_date = min(start_date + timedelta(days=self.chunk_size_days), end_date)
            chunks.append((start_date, chunk_end_date))
            start_date = chunk_end_date

        # Execute API calls in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for start, end in chunks:
                # Update params with the new date range for the current chunk
                chunk_params = params.copy()
                chunk_params['startDate'] = start.strftime('%Y-%m-%d')
                chunk_params['endDate'] = end.strftime('%Y-%m-%d')
                
                futures.append(executor.submit(self.fetch_data_chunk, url, chunk_params))

            # Collect results as they complete
            for future in as_completed(futures):
                try:
                    result = future.result()
                    all_data.extend(result)
                except requests.HTTPError as e:
                    print(f"HTTP error occurred: {e}")

        return all_data

    def get_equity_data(self, symbol, start_date, end_date, interval='min'):
        """
        Fetches equity data from the API in batches.

        :param symbol: The symbol for which data is requested.
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        :param interval: The data interval ('min' for minute-level, 'D' for daily).
        :return: The combined JSON response from the API.
        """
        url = f"{self.base_url}/getEquityData"
        params = {
            'symbol': symbol,
            'startDate': start_date,
            'endDate': end_date,
            'interval': interval
        }
        
        return self.fetch_data_in_batches_parallel(url, params)

    def get_crypto_data(self, symbol, start_date, end_date, interval='min'):
        """
        Fetches crypto data from the API in batches.

        :param symbol: The symbol for which data is requested.
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        :param interval: The data interval ('min' for minute-level, 'D' for daily).
        :return: The combined JSON response from the API.
        """
        url = f"{self.base_url}/getCryptoData"
        params = {
            'symbol': symbol,
            'startDate': start_date,
            'endDate': end_date,
            'interval': interval
        }
        
        return self.fetch_data_in_batches_parallel(url, params)
