from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def calculate_value_assets(portfolio: dict) -> dict:
    result = {}
    for asset_name, number_coins in portfolio.items():
        asset_value = cg.get_price(ids=asset_name, vs_currencies='usd')
        portfolio_asset_value = asset_value[asset_name]['usd'] * number_coins
        result[asset_name] = portfolio_asset_value
    return result


def calculate_total_value_portfolio(value_assets_portfolio: dict) -> float:
    total_value = 0
    for value in value_assets_portfolio.values():
        total_value += value
    return total_value


def get_price_coin(id_coin: str, currency: str) -> dict:
    coin_price = cg.get_price(ids=id_coin, vs_currencies=currency)
    return coin_price
