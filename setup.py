from setuptools import setup, find_packages

setup(
    name='backtest_api_client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A client library to interact with the backtest Flask API',
    author='Sujal',
    author_email='0987sujals@gmail.com',
    url='https://github.com/yasho-7/backtest_api_client',
)
