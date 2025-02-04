#!/home/oriyia/.virtualenvs/crypto_portfolio/bin/python3
import json
import math
import sys
from datetime import date
import math

from deposits import DEPOSITS
from portfolio_value import (calculate_total_value_portfolio,
                             calculate_value_assets, get_price_coin)


class Portfolio:
    def __init__(self):
        self.asset_proportions = {
            "BTC": 0.10,  # 0.25
            "BNB": 0.05,
            "ETH": 0.1,  # 0.18
            "DOT": 0.05,
            "NEAR": 0.05,
            "ADA": 0.05,
            "ATOM": 0.05,
            "MATIC": 0.08,  # 0.1
            "GRT": 0.04,
            "AGIX": 0.03,
            "TON": 0.03,
            "SNX": 0.04,
            "ROSE": 0.03,
            "IMX": 0.04,
            "INJ": 0.03,
            "FTM": 0.03,
            "TIA": 0.08,
            "SOL": 0.08,
            "AVAX": 0.04
        }
        self.cash = 120
        self.cash_rub = 15000
        self.number_averages = 1
        self.number_coins = {
            "bitcoin": 0.03538349,
            "ethereum": 0.4567294,
            "cardano": 205.4967,
            "cosmos": 28.0603,
            "binancecoin": 0.819723,
            "matic-network": 190.13367015,
            "polkadot": 43.83306,
            "near": 129.46945,
            "aave": 0,
            "acala": 32.168,
        }


def check_proportions_assets(asset_proportions: dict) -> bool:
    check_result = False
    amount_assets = 0
    for value in asset_proportions.values():
        amount_assets += value
    if math.isclose(amount_assets, 1, rel_tol=1e-7):
        check_result = True
    return check_result


def calculate_purchase_prices(asset_proportions: dict, cash: int) -> dict:
    purchase_prices = {}
    dollar_rate = get_price_coin("tether", "rub")
    cash_dollar = math.floor(cash / dollar_rate["tether"]["rub"])
    for asset_name, proportion in asset_proportions.items():
        purchase_price = proportion * cash_dollar
        purchase_prices[asset_name] = purchase_price
    return purchase_prices


def calculate_total_amount_deposits(deposits: dict) -> float:
    total_amount = 0
    for value in deposits.values():
        total_amount += value
    return total_amount


def update_profitability_results_file(profitability: float):
    today = date.today()
    with open("profitability_results.json", "r") as file:
        data = json.load(file)

    data[str(today)] = profitability

    with open("profitability_results.json", "w") as file:
        json.dump(data, file)


def main():
    portfolio = Portfolio()
    check_result = check_proportions_assets(portfolio.asset_proportions)
    if not check_result:
        print("Условия проверки суммы активов не пройдены")
        sys.exit()

    purchase_prices = calculate_purchase_prices(
        portfolio.asset_proportions, portfolio.cash_rub
    )
    print(purchase_prices)

    value_assets = calculate_value_assets(portfolio.number_coins)
    print(value_assets)
    total_value_portfolio = calculate_total_value_portfolio(value_assets)
    print(f"Общая стоимость активов: ${total_value_portfolio}")

    dollar_rate = get_price_coin("tether", "rub")
    print(dollar_rate)
    value_assets_rub = dollar_rate["tether"]["rub"] * total_value_portfolio
    print(f"Рублей: {value_assets_rub}")

    total_deposits = calculate_total_value_portfolio(DEPOSITS)
    print(f"Общая сумма пополнений: {total_deposits}")

    profitability = (total_value_portfolio - total_deposits) / total_deposits * 100
    print(f"Доходность: {profitability}")

    update_profitability_results_file(profitability)


if __name__ == "__main__":
    # main()
    sums = 0
    for value in DEPOSITS.values():
        if isinstance(value, list):
            sums += sum(value)
        else:
            sums += value
    print(f"Value: {sums}")
