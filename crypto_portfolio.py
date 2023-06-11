#!/usr/bin/python3
import sys
import math


class Portfolio():
    def __init__(self):
        self.asset_proportions = {
                'BTC': 0.3,
                'BNB': 0.10,
                'ETH': 0.25,
                'DOT': 0.05,
                'NEAR': 0.05,
                'ADA': 0.05,
                'ATOM': 0.05,
                'MATIC': 0.15
        }
        self.cash = 120
        self.number_averages = 1


def check_proportions_assets(asset_proportions: dict) -> bool:
    check_result = False
    amount_assets = 0
    for value in asset_proportions.values():
        amount_assets += value
    print(amount_assets)
    if math.isclose(amount_assets, 1, rel_tol=1e-7):
        check_result = True
    return check_result


def calculate_purchase_prices(asset_proportions: dict, cash: int) -> dict:
    purchase_prices = {}
    for asset_name, proportion in asset_proportions.items():
        purchase_price = proportion * cash
        purchase_prices[asset_name] = purchase_price
    return purchase_prices


def main():
    portfolio = Portfolio()
    check_result = check_proportions_assets(portfolio.asset_proportions)
    if not check_result:
        print("Условия проверки суммы активов не пройдены")
        sys.exit()

    purchase_prices = calculate_purchase_prices(portfolio.asset_proportions, portfolio.cash)
    print(purchase_prices)


if __name__ == "__main__":
    main()
