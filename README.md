# 🛒 Price Drop Alerter

A Python script that monitors product prices and sends you an email alert when the price drops.

---

## 📌 What it does

- Scrapes the price of a product from a webpage
- Saves the price locally to track changes
- Compares the current price with the last saved price
- Sends an **email alert** if a price drop is detected
- Runs automatically every hour using a scheduler

---

## 🛠️ Tech Stack

- **requests** — fetches the webpage
- **BeautifulSoup** — parses HTML to extract the price
- **json** — saves and loads price data locally
- **smtplib** — sends email alerts via Gmail
- **schedule** — runs the price check automatically
- **python-dotenv** — keeps credentials secure

---

## 🚀 How to run

**1. Clone the repository**
```bash
git clone https://github.com/vanshika15manchanda/price-drop-alerter.git
cd price-drop-alerter
```

**2. Install dependencies**
```bash
pip install requests beautifulsoup4 schedule python-dotenv
```

**3. Create a `.env` file** in the project folder
```
EMAIL=your_email@gmail.com
PASSWORD=your_gmail_app_password
```

> To get a Gmail App Password: Google Account → Security → 2-Step Verification → App Passwords

**4. Run the script**
```bash
python main.py
```

The script will check the price every hour and email you if it drops.

---

## 📁 Project Structure

```
price-drop-alerter/
│
├── main.py          # Main script
├── data.json        # Stores the last known price (auto-created)
├── .env             # Your credentials (never share this)
└── README.md        # This file
```

---

## ⚠️ Important

- Never upload your `.env` file to GitHub
- Add `.env` to your `.gitignore` file before pushing

```
# .gitignore
.env
data.json
```

---

## 🔮 Future improvements

- Track multiple products at once
- Add SMS / WhatsApp alerts via Twilio
- Build a simple dashboard to view price history
- Support for more websites

---

## 👤 Author

Built by Vanshika Manchanda as a first Python project.
