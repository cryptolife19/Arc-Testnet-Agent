from datetime import datetime
import urllib.request
import json
class ArcAgent:
    def __init__(self):
        self.name = "Arc Testnet AI Agent"

    def get_btc_price(self):
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data['bitcoin']['usd']
        except Exception as e:
            print(f"API Error: {e}")
            return 65000
    def run(self):
        print("=" * 50)
        print(f"{self.name}")
        print("=" * 50)

        now = datetime.now()
        print("Current Time :", now)

        price = self.get_btc_price()

        if price:
            print(f"BTC Price : ${price}")
        else:
            print("Unable to fetch BTC price.")

        print("\nAgent Completed Successfully.")

if __name__ == "__main__":
    agent = ArcAgent()
    agent.run()