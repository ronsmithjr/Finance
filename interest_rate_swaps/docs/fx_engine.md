# 💱 FX Direction: `base_to_quote`

In foreign exchange (FX) trading, setting `direction = base_to_quote` means you're analyzing currency movements from the perspective of the **base currency**.

---

## 📘 Currency Pair Format

- Format: `BASE/QUOTE` (e.g., `EUR/USD`)
- **Base Currency**: The first currency in the pair (`EUR`)
- **Quote Currency**: The second currency in the pair (`USD`)

---

## 📈 What "Base to Quote" Means

- You're evaluating how the **base currency** moves relative to the **quote currency**
- Example: If `EUR/USD` rises from `1.1000` to `1.1200`:
  - The euro (**EUR**) has **strengthened** against the dollar (**USD**)
  - It now takes **more USD to buy one EUR**
- A **long position** in `EUR/USD` means you're betting the **EUR will rise** relative to USD

---

## 🔄 Use in Trading Systems

Setting `direction = base_to_quote` helps:

- Normalize currency movements to the base currency’s perspective
- Standardize calculations like:
  - Pip values
  - Returns
  - Volatility
- Align with conventions used in platforms like MetaTrader or CME Globex

---

## 🛠️ Optional Python Integration

You can use this direction setting in a Python FX module to:

- Calculate returns from the base currency’s view
- Build normalized price series
- Create modular trading logic

---

