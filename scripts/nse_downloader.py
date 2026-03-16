import requests
import pandas as pd
from datetime import datetime
import os

url = "https://archives.nseindia.com/products/content/sec_bhavdata_full.csv"

headers = {
 "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

file_path = "C:/Users/Arnv/Documents/DharmQuant-Data/01- equities/nse_daily/bhavcopy.csv"

with open(file_path, "wb") as f:
    f.write(r.content)

df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

df = df.rename(columns={
 "SYMBOL":"symbol",
 "OPEN_PRICE":"open",
 "HIGH_PRICE":"high",
 "LOW_PRICE":"low",
 "CLOSE_PRICE":"close",
 "TTL_TRD_QNTY":"volume"
})

df["source"] = "NSE"

df.to_parquet("C:/Users/Arnv/Documents/DharmQuant-Data/01- equities/nse_daily/latest.parquet")