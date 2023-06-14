#!/home/oriyia/.virtualenvs/crypto_portfolio/bin/python3
import sys
import math

from portfolio_value import calculate_value_assets, calculate_total_value_portfolio, get_price_coin
from deposits import DEPOSITS


class Portfolio():
    def __init__(self):
        self.asset_proportions = {
                'BTC': 0.3,
                'BNB': 0.10,
                'ETH': 0.2,
                'DOT': 0.05,
                'NEAR': 0.05,
                'ADA': 0.05,
                'ATOM': 0.05,
                'MATIC': 0.1,
                'IMX': 0.02,
                'ROSE': 0.08
        }
        self.cash = 120
        self.number_averages = 1
        self.number_coins = {
            'bitcoin': 0.03538349,
            'ethereum': 0.4567294,
            'cardano': 205.4967,
            'cosmos': 28.0603,
            'binancecoin': 0.819723,
            'matic-network': 190.13367015,
            'polkadot': 43.83306,
            'near': 129.46945,
            'aave': 0,
            'acala': 32.168,
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
    for asset_name, proportion in asset_proportions.items():
        purchase_price = proportion * cash
        purchase_prices[asset_name] = purchase_price
    return purchase_prices


def calculate_total_amount_deposits(deposits: dict) -> float:
    total_amount = 0
    for value in deposits.values():
        total_amount += value
    return total_amount


def main():
    portfolio = Portfolio()
    check_result = check_proportions_assets(portfolio.asset_proportions)
    if not check_result:
        print("Условия проверки суммы активов не пройдены")
        sys.exit()

    purchase_prices = calculate_purchase_prices(portfolio.asset_proportions, portfolio.cash)
    print(purchase_prices)

    value_assets = calculate_value_assets(portfolio.number_coins)
    print(value_assets)
    total_value_portfolio = calculate_total_value_portfolio(value_assets)
    print(f"Общая стоимость активов: ${total_value_portfolio}")

    dollar_rate = get_price_coin('tether', 'rub')
    print(dollar_rate)
    value_assets_rub = dollar_rate['tether']['rub'] * total_value_portfolio
    print(f"Рублей: {value_assets_rub}")

    total_deposits = calculate_total_value_portfolio(DEPOSITS)
    print(f"Общая сумма пополнений: {total_deposits}")

    profitability = (total_value_portfolio - total_deposits) / total_deposits * 100
    print(f"Доходность: {profitability}")


if __name__ == "__main__":
    main()
