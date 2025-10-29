# formosa OJ 1855
def usd_to_twd(usd_amount, rate):
  """
  將美元金額 (usd_amount) 根據匯率 (rate) 轉換為台幣金額。
  四捨五入到最接近的整數。
  """
  twd_amount = usd_amount * rate
  return round(twd_amount)

# 獲取使用者輸入的匯率
exchange_rate = float(input())

# 獲取使用者輸入的美元價格列表 (用空白鍵分隔)
usd_prices_input = input()

# 將輸入的價格字串分割並轉換為數字列表
usd_prices = [float(price.strip()) for price_str in usd_prices_input.split() for price in [price_str]]

# 使用函式將美元價格列表轉換為台幣價格列表
twd_prices = [usd_to_twd(price, exchange_rate) for price in usd_prices]

# 印出結果
for i in range(len(usd_prices)):
    print(f"us_price:{usd_prices[i]:.0f}, tw_price:{twd_prices[i]}")