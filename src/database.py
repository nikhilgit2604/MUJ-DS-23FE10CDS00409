import sqlite3
from datetime import datetime


DATABASE_NAME = "complaints.db"


def create_database():
    """Create the complaints table if it does not exist."""

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint TEXT NOT NULL,
            category TEXT,
            sentiment TEXT,
            sentiment_score REAL,
            priority TEXT,
            keywords TEXT,
            llm_analysis TEXT,
            created_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_complaint(result, complaint):
    """Save a complaint analysis result to the database."""

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    sentiment = result["sentiment"]
    urgency = result["urgency"]

    cursor.execute("""
        INSERT INTO complaints (
            complaint,
            category,
            sentiment,
            sentiment_score,
            priority,
            keywords,
            llm_analysis,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        complaint,
        result["category"],
        sentiment["sentiment"],
        sentiment["score"],
        urgency["priority"],
        ", ".join(result["keywords"]),
        result["llm_analysis"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_complaints():
    """Retrieve all stored complaints."""

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            complaint,
            category,
            sentiment,
            sentiment_score,
            priority,
            keywords,
            llm_analysis,
            created_at
        FROM complaints
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows