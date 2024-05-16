import requests
import pandas as pd
# import xlwings as xw
# import time
url ="https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
headers = {"Accept-Encoding":"gzip, deflate, br, zstd",
           "Accept-Language" :"en-US,en;q=0.9",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
# while True:
session = requests.Session()
data = session.get(url,headers=headers).json()["records"]["data"]

ocdata =[]
for i in data:
        for j,k in i.items():
            if j=="CE" or j=="PE":
                info = k
                info["instrumentType"]=j
                ocdata.append(info)
                
df=pd.DataFrame(ocdata)
    # wb = xw.Book("optionchaintracker.xlsx")
    # st = wb.sheets("banknifty")
    # st.range("A1").value = df

    # # time.sleep(10)
print(df)