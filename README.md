# 📋 Clipboard Hijacker – Red Team Simulation Tool

> **Author:** Joseph Ogbekile (`@OgbekileX`)  
> **Version:** 1.0  
> **License:** MIT  
> **GitHub:** [github.com/OgbekileX/clipboard-hijacker](https://github.com/OgbekileX/clipboard-hijacker)

---

## 🧠 Overview

This tool is a **clipboard hijacking simulation utility** written in Python, designed to assist **red teamers, penetration testers, and malware researchers** in simulating clipboard-based cryptocurrency wallet address hijacks in controlled environments.

It replaces copied wallet addresses with attacker-controlled wallets and can optionally report replacement events via a Telegram bot.

> ❗ This project is strictly for **educational, research, and ethical simulation purposes** in authorized red team labs or personal environments.

---

## ⚠️ Ethical Disclaimer

> This tool is intended for **authorized penetration testing**, **cybersecurity training**, and **blue team detection development** only.

Do **not** deploy or distribute this software on systems or networks without **explicit, written consent**. Misuse of this tool may result in **criminal prosecution**, and the author assumes **no liability** for unethical or illegal use.

---

## 🚀 Features

- ✅ Real-time clipboard monitoring
- 🪙 Detects cryptocurrency wallet addresses using regex patterns
- 🔁 Automatically replaces matching addresses with attacker-controlled values
- 📲 Sends alert logs to Telegram (optional)
- ⚙️ Lightweight, open-source, Python-based

---

## 💰 Supported Cryptocurrencies

This simulation tool can detect and replace the following wallet formats:

| Coin | Wallet Address Used |
|------|---------------------|
| **BTC** | `bc1qexample000000000000000000000000000000000` |
| **ETH** | `0x000000000000000000000000000000000000dEaD` |
| **BNB** | `0x000000000000000000000000000000000000dEaD` |
| **LTC** | `ltc1qexample0000000000000000000000000000000` |
| **TRX** | `TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` |
| **SOL** | `11111111111111111111111111111111` |
| **ADA** | `addr1qexample000000000000000000000000000000000000000000000000000000` |
| **DOGE** | `DExampleWalletAddr000000000000000000` |
| **XRP** | `rExampleWalletAddress000000000000000` |

---

## 📦 Installation

Ensure Python 3 is installed on your machine. Then:

### 1. Clone the Repository
git clone https://github.com/OgbekileX/clipboard-hijacker.git

cd clipboard-hijacker

### 2. Install Python Dependencies
pip install -r requirements

### ⚙️ Telegram Bot Setup (Optional)
To receive real-time replacement logs via Telegram:

## Step 1: Create a Telegram Bot
Open Telegram
Search for @BotFather
Create a new bot and copy the bot token

## Step 2: Get Your Telegram Chat ID
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
Copy your chat_id.

## Step 3: Add to hijacker.py
bot_token = "YOUR_BOT_TOKEN"

chat_id = "YOUR_CHAT_ID"

The script will now send a message each time a clipboard replacement occurs.

### ▶️ How to Run the Tool
python hijacker.py

You can use tools like tmux, screen, nohup, or autostart methods if you wish to run it persistently.

### 🔧 How to Customize Wallet Addresses
You can easily replace the default attacker wallet addresses with your own by editing the main script.

## Steps:
Open the hijacker.py file using any code or text editor:

*nano hijacker.py*

or

*code hijacker.py*       # if you're using VS Code

Find the section with wallet mappings:

wallet_map = {

    |"BTC": "bc1qexample000000000000000000000000000000000",|
    
    |"ETH": "0x000000000000000000000000000000000000dEaD",|
    
    "BNB": "0x000000000000000000000000000000000000dEaD",
    
    "LTC": "ltc1qexample0000000000000000000000000000000",
    
    ...
}

Replace any address with your own (for lab simulation), e.g.:


"BTC": "bc1qNEWyourBTCwalletaddresshere"

Save and exit the file.


You’re now simulating clipboard hijacking with your own crypto addresses.



### 🛡️ For Blue Teams: How to Defend Against Clipboard Hijacking
✅ Monitor clipboard access with endpoint detection tools

✅ Use behavior-based EDR or Sysmon to detect frequent clipboard access

✅ Alert on processes replacing wallet patterns in user clipboard data

✅ Enforce strict allowlisting of Python and scripting tools

✅ Train users to verify pasted addresses before sending crypto

This simulation tool can assist in developing detections and preparing defenses.

### 🔐 License
This project is licensed under the MIT License.
© 2025 Joseph Ogbekile

### 👤 About the Author
Joseph Ogbekile
Cybersecurity Analyst | Red Team Simulation Developer
GitHub: @OgbekileX

🔗 Connect with me to collaborate on ethical red teaming and blue team detection tooling.

⭐ Star & Share
If you find this useful for training or research, give the repo a ⭐ and help others learn responsibly.
