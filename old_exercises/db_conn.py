import psycopg2


connection_params = {
     'host':'localhost',
     'database':'messages_db',
     'user':'alexis_jover',
	 'password': 'your_password',    # Replace with your password
     'port': 5432
     }


try:
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()
    print("Connected to PostgreSQL successfully!")
    
    # Test the connection
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"PostgreSQL version: {version[0]}")
    
except Exception as error:
    print(f"Error connecting to PostgreSQL: {error}")