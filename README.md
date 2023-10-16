# Simple-RaV-Calculator-for-Portfolio-or-Treasury-Bills
The Value at Risk (VaR) Calculator is a Python script designed for financial risk management. It serves as a powerful tool for assessing potential financial losses with a specified confidence level, taking into account various risk factors such as currency exchange rates and volatility.

## Usage

### Prerequisites

- Python
- NumPy (for mathematical operations)

### Running the Code

1. Clone this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script with the following command:

   ```bash
   python var_calculator.py [-m RISK_FACTOR]

    Replace RISK_FACTOR with 1 for one risk factor or 2 for two risk factors.

### Parameters

    amount: The amount of the investment or portfolio.
    exchange_rate: The exchange rate used for currency conversion.
    daily_returns: A list of daily returns used to calculate volatility.
    confidence_level: The desired confidence level for the VaR calculation (e.g., 95%).
    risk_factor_n: The number of risk factors considered (1 or 2).
    exchange_rate_bills: A specific exchange rate for Treasury Bills (used only if risk_factor_n is 2).
    correlation_coefficient: A coefficient for measuring the correlation between risk factors (used only if risk_factor_n is 2).
