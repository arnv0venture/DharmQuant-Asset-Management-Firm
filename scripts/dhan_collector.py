from dhanhq import dhanhq
import pandas as pd

client_id = "1108964492"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzczNzcxMjg1LCJpYXQiOjE3NzM2ODQ4ODUsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTA4OTY0NDkyIn0.DiZLmwktzd9RTQfCi3dofB-YlugKaqJHWRkMcxKVuzcdPU5C06LZxt6AU_28aF0_ZPjOHRO58qaGoqMmLZCwPQ"

dhan = dhanhq(client_id, access_token)

data = dhan.intraday_minute_data(
    security_id="1333",
    exchange_segment="NSE_EQ",
    instrument_type="EQUITY"
)

df = pd.DataFrame(data)

df.to_parquet("../DharmQuant_Data/live_market/dhan_minute/reliance.parquet")