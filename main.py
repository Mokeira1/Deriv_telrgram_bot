import os

print("================================")
print(" Deriv Telegram Bot Starting...")
print("================================")

BOT_TOKEN = os.getenv("BOT_TOKEN")
DERIV_API_TOKEN = os.getenv("DERIV_API_TOKEN")

if BOT_TOKEN:
    print("✅ Telegram token found")
else:
    print("❌ BOT_TOKEN is missing")

if DERIV_API_TOKEN:
    print("✅ Deriv API token found")
else:
    print("❌ DERIV_API_TOKEN is missing")

print("Bot initialized successfully.")
