import sys
import numpy as np

def calculate_var(amount, exchange_rate, daily_returns, confidence_level, risk_factor_n=1, exchange_rate_bills=0.0, correlation_coefficient=0.0):
    volatility = np.std(daily_returns)
    
    if risk_factor_n == 1:
        var = amount * exchange_rate * volatility * 1.65
        return var
    elif risk_factor_n == 2:
        var1 = amount * exchange_rate * exchange_rate_bills * 1.65
        var2 = amount * exchange_rate * volatility * 1.65
        total_var = pow(pow(var1, 2) + pow(var2, 2) - (2 * correlation_coefficient * var1 * var2), 1/2)
        return total_var

if __name__ == "__main__":
    main_settings = {
        "risk_factor_n": 1,
        "amount": 1000,
        "exchange_rate": 1.05578,
        "exchange_rate_bills": 0.00602,
        "correlation_coefficient": 0.25
    }
    
    if len(sys.argv) > 2:
        if sys.argv[1] == "-m" and sys.argv[2]:
            main_settings["risk_factor_n"] = int(sys.argv[2])

    daily_returns = [1.0560, 1.0522, 1.0509, 1.0526, 1.0617, 1.0603]
    confidence_level = 95

    var = calculate_var(
        amount=main_settings["amount"],
        exchange_rate=main_settings["exchange_rate"],
        daily_returns=daily_returns,
        confidence_level=confidence_level,
        risk_factor_n=main_settings["risk_factor_n"],
        exchange_rate_bills=main_settings["exchange_rate_bills"],
        correlation_coefficient=main_settings["correlation_coefficient"]
    )

    if main_settings["risk_factor_n"] == 1:
        print(f"VaR: {var:.2f}")
    elif main_settings["risk_factor_n"] == 2:
        print(f"Total VaR: {var:.2f}")
