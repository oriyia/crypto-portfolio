#!/usr/bin/python3
share_assets = {
        'BTC': 0.3,
        'BNB': 0.10,
        'ETH': 0.25,
        'DOT': 0.05,
        'NEAR': 0.05,
        'ADA': 0.05,
        'ATOM': 0.05,
        'MATIC': 0.15
}

cash = 100
number_averages = 1


def checking_proportion_assets(assets):
    sum = 0
    for share in share_assets.values():
        sum = sum + share
    return sum


def creating_list_purchase_price_montly():

    list_purchase_price_monthly = {}

    for asset_name, fraction in share_assets.items():
        asset_purchase_price = fraction * cash
        list_purchase_price_monthly[asset_name] = asset_purchase_price

    return list_purchase_price_monthly


def creating_list_purchase_price_once(list_purchase_price_monthly):

    list_purchase_price_once = {}

    for asset_name, price in list_purchase_price_monthly.items():
        asset_purchase_price = price / number_averages
        list_purchase_price_once[asset_name] = asset_purchase_price

    return list_purchase_price_once


def final_calculations():

    sum_assets = checking_proportion_assets(share_assets)

    print(sum_assets)
    list_purchase_price_monthly = creating_list_purchase_price_montly()
    list_purchase_price_once = creating_list_purchase_price_once(list_purchase_price_monthly)
    print(list_purchase_price_monthly)
    # if sum_assets == 1:
    #     list_purchase_price_monthly = creating_list_purchase_price_montly()
    #     list_purchase_price_once = creating_list_purchase_price_once(list_purchase_price_monthly)
    #     print(list_purchase_price_monthly)
    # else:
    #     print("Сумма актива не равна 1!")


final_calculations()
