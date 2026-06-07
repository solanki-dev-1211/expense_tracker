import sqlite3

DB_NAME="expenses.db"

class Database:
    @staticmethod
    def connect():
        return sqlite3.connect(DB_NAME)
    
    @staticmethod
    def initialize():
        
        conn=Database.connect()
        cursor=conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            expense_date TEXT NOT NULL,
            notes TEXT)
            """)
        
        conn.commit()
        conn.close()