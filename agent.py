from datetime import datetime

class ArcAgent:
    def __init__(self):
        self.name = "Arc Testnet AI Agent"

    def get_btc_price(self):
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "usd"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            price = response.json()["bitcoin"]["usd"]
            return price
        else:
            return None

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