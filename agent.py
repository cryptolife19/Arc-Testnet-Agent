from datetime import datetime
import urllib.request
import json

class ArcAgent:
    def __init__(self):
        self.name = "Arc Testnet AI Agent"

    def get_btc_data(self):
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                price = data['bitcoin']['usd']
                change_24h = data['bitcoin'].get('usd_24h_change', 0)
                return price, change_24h
        except Exception as e:
            print(f"API Error: {e}")
            return 65000, 0.5  # Fallback data

    def generate_recommendation(self, price, change):
        # ট্রেড সাজেশন লজিক
        if change > 2.0:
            status = "STRONG BUY"
            suggestion = "Market trend is bullish (+2%+). Good time for long trade!"
            color = "#22c55e" # Green
        elif change < -2.0:
            status = "RISKY / HOLD"
            suggestion = "Market is dropping (-2%+). Better to wait or set stop-loss!"
            color = "#ef4444" # Red
        else:
            status = "NEUTRAL / SIDEWAYS"
            suggestion = "Price is stable. Small scalp trades recommended."
            color = "#eab308" # Yellow

        return {
            "btc_price": f"${price:,.2f}",
            "change_24h": f"{change:.2f}%",
            "status": status,
            "suggestion": suggestion,
            "color": color,
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def run(self):
        price, change = self.get_btc_data()
        result = self.generate_recommendation(price, change)
        
        # HTML ফ্রন্টএন্ডের জন্য JSON ফাইলে সেভ
        with open("btc_data.json", "w") as f:
            json.dump(result, f, indent=4)
            
        print("Data updated successfully in btc_data.json:", result)

if __name__ == "__main__":
    agent = ArcAgent()
    agent.run()