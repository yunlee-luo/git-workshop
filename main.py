def usd_to_twd(usd_amount, rate):
  
  twd_amount = usd_amount * rate
  return round(twd_amount)

exchange_rate = float(input())

usd_prices_input = input()

usd_prices = [float(price.strip()) for price_str in usd_prices_input.split() for price in [price_str]]

twd_prices = [usd_to_twd(price, exchange_rate) for price in usd_prices]

for i in range(len(usd_prices)):
    print(f"us_price:{usd_prices[i]:.0f}, tw_price:{twd_prices[i]}")