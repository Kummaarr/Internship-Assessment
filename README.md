
# Medak District Court - Case Data Fetcher & Dashboard

## 🌐 Court Chosen
**Medak District Court** - https://districts.ecourts.gov.in/medak

## 🚀 Features
- Search by Case Type, Number & Year
- Scrapes party names, filing dates, next hearing date
- Displays latest judgment/order PDF (if available)
- Logs every search to SQLite
- Simple and user-friendly UI
- Handles invalid case input gracefully

## 🧠 CAPTCHA Strategy
Medak District Court doesn't use reCAPTCHA; hidden tokens were handled using cookies and hidden fields via BeautifulSoup.

## 🛠 Setup
```bash
git clone https://github.com/your-username/medak-court-data-fetcher.git
cd medak-court-data-fetcher
pip install -r requirements.txt
python run.py
```

## 🎥 Demo Video
[Watch here](https://www.youtube.com/watch?v=your_video_id)
