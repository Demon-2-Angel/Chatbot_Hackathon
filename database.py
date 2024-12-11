import sqlite3
import json

# Initialize database connection
conn = sqlite3.connect("chatbot_data.db")
cursor = conn.cursor()

# Function to create database tables
def setup_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        chatbot_response TEXT,
        evaluation JSON
    )
    """)
    conn.commit()

# Function to save a conversation entry
def save_conversation(user_input, chatbot_response, evaluation):
    cursor.execute("""
    INSERT INTO conversations (user_input, chatbot_response, evaluation)
    VALUES (?, ?, ?)
    """, (user_input, chatbot_response, json.dumps(evaluation)))
    conn.commit()

# Function to close the database connection
def close_database():
    conn.close()
