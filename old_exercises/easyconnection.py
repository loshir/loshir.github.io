import pandas as pd
from sqlalchemy import create_engine


connection_string = "postgresql://alexis_jover:your_password@localhost:5432/messages_db"
engine = create_engine(connection_string)

df = pd.read_sql_query("SELECT * FROM public.telegram_messages_2", engine)

engine.dispose()