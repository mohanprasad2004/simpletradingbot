# 📈 My Quant Trading Journey: SMA Trading Simulation

Welcome to my first step into **quantitative trading** and **algorithmic strategy development**!  
This project implements a **Simple Moving Average (SMA) trading strategy** using real-time financial data.

---

## 🚀 Overview

This Python project demonstrates:
- Building **modular trading strategies** (starting with SMA crossovers).
- Simulating **buy/sell signals** based on price data.
- Executing trades using a **mock API** and tracking balance updates.
- Fetching **real-time price data** using Yahoo Finance (`yfinance`).

🔎 **Key Concepts:**
- Object-Oriented Programming (OOP) in Python  
- Financial Data Handling  
- Trading Logic Implementation  
- Backtesting Concepts  

---

## 📚 How It Works

### 🔨 Components

1️⃣ **`MyTradingStrategy` (Base Class)**  
Defines a generic trading strategy structure. Intended to be overridden.

2️⃣ **`MySMATradingStrategy` (Derived Class)**  
Implements a simple moving average crossover strategy:
- Uses **short window** and **long window** periods.
- Generates:
  - `"buy"` if short SMA > long SMA,
  - `"sell"` if short SMA < long SMA,
  - `"hold"` otherwise.

3️⃣ **`MyTrade`**  
Represents a single trade:
- Contains strategy name, signal, amount, and timestamp.
- Executes and logs trade details.

4️⃣ **`MockTradingAPI`**  
A simple mockup for placing buy/sell trades:
- Tracks balance.
- Prints trade outcomes.

5️⃣ **`MyTradingSystem`**  
The heart of the simulation:
- Fetches latest price data from Yahoo Finance.
- Runs the strategy to generate signals.
- Executes trades through the mock API.

---

### 📈 Flow

1. Initialize a trading strategy (SMA with chosen window sizes).
2. Set up a mock API with a starting balance.
3. Create a trading system to:
   - Fetch live price data.
   - Generate trade signals.
   - Execute trades and update balance.
4. Loop over a time period to simulate trading decisions.

---

### ⚙️ Setup Instructions

1️⃣ **Install Required Packages**
```bash
pip install yfinance
