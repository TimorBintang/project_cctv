# 📹 Balikpapan CCTV Monitoring Data Pipeline

A modular, robust, and automated ETL (Extract, Transform, Load) pipeline built with Python and PostgreSQL to monitor 82 public CCTV video streams across Balikpapan City.

## 📌 Features
- **Automated Stream Checking:** Periodically checks HTTP response status and payload size for 82 CCTV streams.
- **Anomaly Detection:** Identifies offline streams, server errors, or corrupted/low-resolution feeds (`ANOMALI/BURIK`).
- **Data Access Layer (DAL):** Clean modular design separating orchestration (`main.py`), HTTP fetching (`fetcher.py`), and PostgreSQL interaction (`db.py`).
- **Connection Efficiency:** Reuses a single PostgreSQL connection per iteration cycle to prevent database socket exhaustion.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Database:** PostgreSQL
- **Libraries:** `requests`, `psycopg2`, `python-dotenv`

## 📁 Project Structure
```text
project_cctv/
├── .env.example       # Environment variables template
├── .gitignore         # Files ignored by Git
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
├── main.py            # Pipeline orchestrator
├── db.py              # PostgreSQL database module
├── fetcher.py         # HTTP fetching & status transformer
└── data.py            # CCTV endpoints dictionary