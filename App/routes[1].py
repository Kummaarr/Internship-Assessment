
from flask import render_template, request
from app import app
from utils.scraper import fetch_case_details
import sqlite3

@app.route("/", methods=["GET", "POST"])
def home():
    data, error = None, None
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_no = request.form["case_no"]
        case_year = request.form["case_year"]
        try:
            data = fetch_case_details(case_type, case_no, case_year)
            log_query(case_type, case_no, case_year, data)
        except Exception as e:
            error = str(e)
    return render_template("index.html", data=data, error=error)

def log_query(case_type, case_no, case_year, raw_data):
    conn = sqlite3.connect("db/court_queries.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS queries (id INTEGER PRIMARY KEY AUTOINCREMENT, case_type TEXT, case_no TEXT, year TEXT, data TEXT)")
    c.execute("INSERT INTO queries (case_type, case_no, year, data) VALUES (?, ?, ?, ?)", (case_type, case_no, case_year, str(raw_data)))
    conn.commit()
    conn.close()
