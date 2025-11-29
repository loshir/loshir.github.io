import sqlite3
import psycopg2
import os

def migrate_postgresql_to_sqlite():
    # PostgreSQL connection (update with your credentials)
    pg_conn = psycopg2.connect(
        host="localhost",
        database="messages_db", 
        user="alexis_jover",
        password="your_password"
    )
    
    # SQLite connection
    sqlite_conn = sqlite3.connect("memories.db")
    
    # Create SQLite table
    sqlite_conn.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        date TEXT,
        name TEXT,
        content TEXT
    )
    """)
    
    # Fetch from PostgreSQL
    pg_cursor = pg_conn.cursor()
    pg_cursor.execute("SELECT id, date, name, content FROM public.telegram_messages_2 ORDER BY id")
    
    # Insert into SQLite in batches (faster for 130K rows)
    batch_size = 1000
    while True:
        rows = pg_cursor.fetchmany(batch_size)
        if not rows:
            break
            
        sqlite_conn.executemany(
            "INSERT INTO messages (id, date, name, content) VALUES (?, ?, ?, ?)",
            rows
        )
        print(f"Migrated {len(rows)} rows...")
    
    # Commit and close
    sqlite_conn.commit()
    sqlite_conn.close()
    pg_conn.close()
    
    print("✅ Migration complete! Check memories.db")

# Run migration
migrate_postgresql_to_sqlite()
