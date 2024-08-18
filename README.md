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
