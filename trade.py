from bitbnspy import bitbns
import json
import requests
key = '549DE16DB78E7A6303EECC12801EFF76'
secretKey = '92E52D62AD4F62C573E1CFC112C33823'
bitbnsObj = bitbns(key, secretKey)
x = bitbnsObj.currentCoinBalance('USDT')
x2 = bitbnsObj.currentCoinBalance('INR')
y = json.dumps(x)
z = json.loads(y)
y2 = json.dumps(x2)
z2 = json.loads(y2)
usdt = z["data"]["availableorderUSDT"]
inr = z2["data"]["availableorderMoney"]
print("-----------------------------------------------\n")
print("Bitbns USDT Bot\n")
print("-----------------------------------------------\n")
print("Your Bitbns USDT Balance:", usdt)
print("Your Bitbns INR Balance:", inr)
sell_qty = int(input("Please Enter your Sell Quantity in USDT:"))
sell_rate = int(input("Please Enter your Sell Rate:"))

if sell_qty > usdt:
    print("The selling qty cannot be more than your USDT Balance!")
if sell_qty <= usdt:
    x1 = bitbnsObj.placeSellOrder('USDT', sell_qty, sell_rate)
    y1 = json.dumps(x1)
    z1 = json.loads(y1)
    print(z1["data"])
    print("Error:", z1["error"])
stopen = input("Press Enter to exit")
