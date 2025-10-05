# main.py
from data_ingestion import create_db_engine, query_data, read_from_web_CSV

# Checking if the function names are now associated with the module
print(create_db_engine.__module__)
print(query_data.__module__)
print(read_from_web_CSV.__module__)
