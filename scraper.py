import requests
from bs4 import BeautifulSoup
import time
import random

#visa slots website
URL = "https://visaslots.info"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}

def check_slots():
    print("🔍 Fetching the website...")
    response = requests.get(URL, headers=HEADERS)

    if response.status_code == 429:
        print("❌ Too many requests! Sleeping for a while...")
        time.sleep(random.randint(60, 120))
        return check_slots()

    if response.status_code != 200:
        print(f"❌ Failed to fetch page. Status Code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")

    if not rows:
        print("❌ No rows found! Website structure might have changed.")
        return

    # slot details for Mumbai VAC
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 5:  # Ensure there are enough columns
            location = columns[0].text.strip()
            visa_type = columns[1].text.strip()
            update_time = columns[2].text.strip()
            earliest = columns[3].text.strip()
            slots = columns[4].text.strip()

            if "MUMBAI VAC" in location:
                print(f"✅ Checked Mumbai VAC: Slots={slots}, Earliest={earliest}, Last Updated={update_time}")
                if slots != "0":  # Notify only if slots are available
                    send_notification(location, slots, earliest, update_time)
                break

def send_notification(location, slots, earliest, update_time):
    message = f"🎉 Visa Slots Available! \n\n📍 Location: {location}\n🟢 Slots: {slots}\n📅 Earliest: {earliest}\n⏳ Last Updated: {update_time}"
    print("🚀 Sending Notification:", message)
    send_telegram_message(message)

# send message via Telegram Bot
def send_telegram_message(message):
    TELEGRAM_BOT_TOKEN = "7548531418:AAE9g_BIZMQSU6c2nbR5b6fBFVMRlj4uH2w"
    TELEGRAM_CHAT_ID = "1257542254"

    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}

    response = requests.post(telegram_url, json=payload)
    if response.status_code == 200:
        print("✅ Telegram Notification Sent Successfully!")
    else:
        print(f"❌ Failed to send Telegram message. Status: {response.status_code}, Response: {response.text}")

while True:
    check_slots()
    sleep_time = random.randint(60, 300)
    print(f"⏳ Sleeping for {sleep_time} seconds before next check...")
    time.sleep(sleep_time)
