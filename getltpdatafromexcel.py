from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger
import pandas as pd
import requests
import xlwings as xw

wb = xw.Book('optionchaintracker.xlsx')
credential = wb.sheets('credential')
angelloginid = credential.range('b1').value
angelpassword = credential.range('b2').value
angelapikey = credential.range('b3').value
angelsecretkey = credential.range('b4').value
angeltoken = credential.range('b5').value


# obj =SmartConnect(api_key=angelapikey)
# data = obj.generateSession(angelloginid,angelpassword,pyotp.TOTP(angeltoken).now())
# refreshToken = data['data']['refreshToken']
# feedToken = obj.getfeedToken()
# print(feedToken)

api_key = 'JD6fxVB3'
username = 'K50310615'
pwd = '1289'
smartApi = SmartConnect(api_key)
try:
    token = "22QTKUSZICB7WG2KN5KWHZQYSE"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

correlation_id = "abcde"
data = smartApi.generateSession(username, pwd, totp)

if data['status'] == False:
    logger.error(data)
    
else:
    # login api call
    # logger.info(f"You Credentials: {data}")
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    # fetch the feedtoken
    feedToken = smartApi.getfeedToken()
    # fetch User Profile
    res = smartApi.getProfile(refreshToken)
    smartApi.generateToken(refreshToken)
    res=res['data']['exchanges']

    #  place order
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": "SBIN-EQ",
            "symboltoken": "3045",
            "transactiontype": "BUY",
            "exchange": "NSE",
            "ordertype": "LIMIT",
            "producttype": "DELIVERY",
            "duration": "DAY",
            "price": "760",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": "1"
            }
        # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        # # Method 2: Place an order and return the full response
        # response = smartApi.placeOrderFullResponse(orderparams)
        # logger.info(f"PlaceOrder : {response}")
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
