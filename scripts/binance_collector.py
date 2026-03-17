import websocket
import json
import pandas as pd
import time

buffer = []

def on_message(ws, message):

    data = json.loads(message)

    trade = {
        "timestamp": data["T"],
        "symbol": data["s"],
        "price": float(data["p"]),
        "quantity": float(data["q"])
    }

    buffer.append(trade)

    if len(buffer) > 5000:
        df = pd.DataFrame(buffer)
        df.to_parquet("C:/Users/Arnv/Documents/DharmQuant-Data/03- crypto/binance_tick/btcusdt.parquet", append=True)
        buffer.clear()

socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(socket, on_message=on_message)

ws.run_forever()