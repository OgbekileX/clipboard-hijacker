# 📋 Clipboard Hijacker – Red Team Simulation Tool

> Developed by **Joseph Ogbekile** (@OgbekileX)  
> Version: 1.0 – July 2025  
> GitHub: [https://github.com/OgbekileX](https://github.com/OgbekileX)

---

## 🎯 Purpose

This is a **Python-based clipboard hijacker simulation tool**, created for **ethical red teaming**, **malware analysis training**, and **detection engineering**.

It monitors copied clipboard content, detects cryptocurrency wallet patterns, and replaces them with predefined attacker-controlled wallets. It can also forward events to Telegram for real-time simulation tracking.

> ⚠️ **This tool is for educational and authorized simulation only. Do not use outside of controlled lab environments or without explicit permission.**

---

## 🔧 Features

- 📋 Continuous clipboard monitoring
- 💰 Detects cryptocurrency wallet formats (BTC, ETH, LTC, TRX, etc.)
- 🔁 Replaces with attacker-specified wallet addresses
- 📡 Sends logs to Telegram via bot API
- 💻 Written in Python 3 – runs on any system with Python installed

---

## 🧪 Supported Wallet Replacements

| Coin | Replaced with |
|------|----------------|
| BTC  | `bc1qgxj7prjxa6v3jhgyfyhjm` |
| ETH / BNB | `0x18d4A160651A04r5tyhge` |
| LTC  | `ltc1qnp44ela6xyxjkhidrserdct` |
| TRX  | `TQCJ3LXazrfVqgDiuytrf6guj` |
| SOL  | `34QzvVjmC9e7E9uytrserfdfyh` |
| ADA  | `addr1q9z57kwnmctf5ekmjhghcftvyhjuglthfukyrvikrjidjnhfcvnjbmgvnfbhdcvf8hi` |
| DOGE | `DBvxf9B15jhtrf6gjmkjgnvbmgntfcvfchdxt` |
| XRP  | `rN6L3Yjnghjumncfbhvbjkmgjnfhvbj` |

---

## 🚀 Setup Instructions

### 1. Install Requirements

```bash
pip install -r requirements.txt
