from bs4 import BeautifulSoup
import json
from database_setup import con, cur
import os
from db_conn import conn, cursor
from datetime import datetime

create_table_query = """
CREATE TABLE IF NOT EXISTS telegram_messages_2 (
    id INTEGER,
    date TIMESTAMP,
    name VARCHAR(255),
    content TEXT
);
"""
cursor.execute(create_table_query)

# Insert data
insert_query = """
INSERT INTO telegram_messages_2 (id, date, name, content) 
VALUES (%s, %s, %s, %s)
"""

def telegram_extraction(data_dir):
    data = []
    last_sender = ""
    
    for filename in os.listdir(data_dir):
        if filename.endswith(".html"):
            html_file = os.path.join(data_dir, filename)
            
            with open(html_file, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, features="lxml")
            
            messages = soup.find_all(id=True)
            
            for m in messages:
                try:
                    id = int(m.attrs["id"].strip("message"))
                    
                    # Check if content exists
                    content_element = m.find(class_="text")
                    if not content_element:
                        continue
                    content = content_element.text.strip()
                    
                    # Check if date exists
                    date_element = m.find(class_="pull_right date details")
                    if not date_element or "title" not in date_element.attrs:
                        continue
                    
                    date_str = date_element.attrs["title"].replace(".", "/")
                    date_str = date_str[:19]
                    date = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
                    
                    # Handle name
                    name_element = m.find(class_="from_name")
                    if name_element:
                        name = name_element.text.strip()
                        last_sender = name
                    else:
                        name = last_sender
                    
                    # Create message data dictionary
                    m_data = {
                        "id": id,
                        "date": date,
                        "name": name,
                        "content": content
                    }
                    data.append(m_data)
                    
                    # Insert into database - FIXED: use m_data instead of data, and date instead of date['date']
                    cursor.execute(insert_query, (m_data['id'], m_data['date'], m_data['name'], m_data['content']))
                    
                except (TypeError, AttributeError, ValueError) as e:
                    print(f"Error processing message: {e}")
                    continue
    
    # Commit and close connection
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"Processed {len(data)} messages")
    return data

# Run the extraction
telegram_extraction("/Users/alexisjover/00_Project/Telegram_raw")
