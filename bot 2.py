from datetime import datetime
import yfinance as yf
import time

class MyTradingStrategy:
    def __init__(self, name=None):
        self.__name = name

    def generate_signal(self, price_data):
        print("overridden")
        return "hold"

    def name(self):
        return self.__name


class MySMATradingStrategy(MyTradingStrategy):
    def __init__(self, shortwindow, longwindow):
        self.__shortwindow = shortwindow
        self.__longwindow = longwindow
        super().__init__("My SMA Trading Strategy")

    def generate_signal(self, price_data):
        if len(price_data) < self.__longwindow:
            print("Not enough data to compute moving averages")
            return "hold"

        short_avg = sum(price_data[-self.__shortwindow:]) / self.__shortwindow
        long_avg = sum(price_data[-self.__longwindow:]) / self.__longwindow

        if short_avg > long_avg:
            return "buy"
        elif short_avg < long_avg:
            return "sell"
        else:
            return "hold"

    @property
    def shortwindow(self):
        return self.__shortwindow

    @property
    def longwindow(self):
        return self.__longwindow


class MyTrade:
    def __init__(self, strategyname, signal, amount):
        self.__strategyname = strategyname
        self.__signal = signal
        self.__amount = amount
        self.__timestamp = datetime.now()

    def execute(self):
        print(f"Executed {self.__signal} trade using {self.__strategyname.name()} strategy for amount {self.__amount} at {self.__timestamp}")

    @property
    def strategyname(self):
        return self.__strategyname

    @property
    def signal(self):
        return self.__signal

    @property
    def amount(self):
        return self.__amount

    @property
    def timestamp(self):
        return self.__timestamp


class MockTradingAPI:
    def __init__(self, balance):
        self.__balance = balance

    def place_order(self, trade, price):
        if trade.signal == "buy" and self.__balance >= trade.amount * price:
            self.__balance -= trade.amount * price
            print(f"Placed a BUY order at {price}, New Balance: {self.__balance:.2f}")
        elif trade.signal == "sell":
            self.__balance += trade.amount * price
            print(f"Placed a SELL order at {price}, New Balance: {self.__balance:.2f}")
        else:
            print("❌ Insufficient balance or invalid signal")

    @property
    def balance(self):
        return self.__balance


class MyTradingSystem:
    def __init__(self, api, strategy, symbol):
        self.__api = api
        self.__strategy = strategy
        self.__symbol = symbol
        self.__price_data = []

    def fetch_price_data(self):
        data = yf.download(tickers=self.__symbol, period='1d', interval='1m')
        if not data.empty:
            price = data['Close'].iloc[-1].item()
            self.__price_data.append(price)
            if len(self.__price_data) > self.__strategy.longwindow:
                self.__price_data.pop(0)
            print(f"📈 Latest price: {price}")
        else:
            print("No new price data fetched.")

    def run(self):
        self.fetch_price_data()
        signal = self.__strategy.generate_signal(self.__price_data)
        print(f"🔎 Generated Signal: {signal}")

        if signal in ["buy", "sell"]:
            trade = MyTrade(self.__strategy, signal, 1)
            trade.execute()
            self.__api.place_order(trade, self.__price_data[-1])

    @property
    def api(self):
        return self.__api

    @property
    def strategy(self):
        return self.__strategy

    @property
    def symbol(self):
        return self.__symbol

    @property
    def balance(self):
        return self.__api.balance


# === Run Your System ===
symbol = 'AAPL'
api = MockTradingAPI(balance=10000)
strategy = MySMATradingStrategy(10, 20)
system = MyTradingSystem(api, strategy, symbol)

for _ in range(50):
    system.run()
    print(f"💰 Remaining balance: {api.balance}")

