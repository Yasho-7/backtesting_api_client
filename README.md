​​**Backtest API Client**

`backtest_api_client` is a Python library that provides a simple client for interacting with a backtest API. It allows users to retrieve equity data for specific symbols and date ranges.

## **Features**

- Fetches equity data for specified symbols.
- Supports different data intervals (`min` for minute-level and `D` for daily).

## **Installation**

To use the `backtest_api_client` in your project, follow these steps:

### **1\. Clone the Repository**

Clone the private GitHub repository to your local machine:

```sh
git clone https://github.com/your-username/backtest_api_client.git
```

Navigate to the cloned directory and install the library:

```sh
cd backtest_api_client
pip install .
```

### **2\. Install Directly from GitHub**

Alternatively, you can install the library directly from GitHub using pip:

```sh
pip install git+https://github.com/Yasho-7/backtesting_api_client.git
```

## **Usage**

Below is an example of how to use the `backtest_api_client`:

```python
from backtest_api_client import BacktestAPIClient

# Create a new instance of the BacktestAPIClient
api = BacktestAPIClient()

# Fetch equity data
data = api.get_equity_data('RELIANCE', '2019-01-01', '2020-01-02')

print(data)
```

## **Output Format**

The output from the API is a list of dictionaries, where each dictionary contains the following fields:

- `c`: The closing price.
- `datetime`: The datetime of the record in GMT.
- `h`: The highest price.
- `l`: The lowest price.
- `o`: The opening price.
- `oi`: The open interest.
- `ti`: The timestamp in UNIX format.
- `vol`: The trading volume.

Example output:

```json
[
  {
    "c": 1518.9,
    "datetime": "Thu, 02 Jan 2020 09:58:00 GMT",
    "h": 1519.0,
    "l": 1518.45,
    "o": 1518.45,
    "oi": 0,
    "ti": 1577959080,
    "vol": 8762
  },
  {
    "c": 1518.7,
    "datetime": "Thu, 02 Jan 2020 09:59:00 GMT",
    "h": 1518.9,
    "l": 1518.5,
    "o": 1518.85,
    "oi": 0,
    "ti": 1577959140,
    "vol": 4935
  }
]
```

## **Development**

### **1\. Set up a Virtual Environment**

It's recommended to use a virtual environment for development:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **2\. Install Development Dependencies**

Install the necessary dependencies for development:

```sh
pip install -r requirements.txt
```

### **3\. Run Tests**

Run the tests to ensure everything is working correctly:

```sh
pytest
```

## **Contributing**

Contributions are welcome\! Please follow the standard GitHub process:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.
