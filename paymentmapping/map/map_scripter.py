import pandas as pd
import time
import sqlite3
from pathlib import Path
import json

def process_csv_data(csv_path):
    df_csv = pd.read_csv(csv_path)
    df_csv.columns = df_csv.columns.str.strip()
    df_csv.columns = df_csv.columns.str.strip().str.replace('-', '').str.replace(r'\s+', ' ', regex=True).str.replace(' ', '_')

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    def fetch_latest_entry():
        cursor.execute("SELECT * FROM map_mappingdata ORDER BY id DESC LIMIT 1")
        latest_entry = cursor.fetchone()
        return latest_entry

    def is_account_number_done(entry_dict):
        return entry_dict.get('Account_Number') == 'Done'

    while True:
        latest_entry = fetch_latest_entry()
        column_names = [description[0] for description in cursor.description]
        latest_entry_dict = {column_names[i]: latest_entry[i] for i in range(len(column_names))}
        del latest_entry_dict['id']
        for key, value in latest_entry_dict.items():
            latest_entry_dict[key] = value.replace(' ', '_')
        if is_account_number_done(latest_entry_dict):
            time.sleep(2)
        else:
            column_mapping = {v: k for k, v in latest_entry_dict.items()}
            filtered_mapping = {key: value for key, value in column_mapping.items() if key != 'NA'}
            # missing_columns = [col for col in filtered_mapping.keys() if col not in df_csv.columns]
            for key, value in latest_entry_dict.items():
                if value == "NA":
                    latest_entry_dict[key] = key
            columns_to_keep = [col for col in latest_entry_dict.values() if col in df_csv.columns]
            df_csv = df_csv[columns_to_keep]
            df_csv.rename(columns=filtered_mapping, inplace=True)
            latest_entry_dict['Account_Number'] = 'Done'
            set_clause = ", ".join(f"{key} = '{value}'" for key, value in latest_entry_dict.items())
            where_clause = f"WHERE id = {latest_entry[0]}"
            update_query = f"UPDATE map_mappingdata SET {set_clause} {where_clause}"
            cursor.execute(update_query)
            conn.commit()
            break
    
    def row_exists_in_database(account_number, vendor_name):
        conn = sqlite3.connect('your_database_name.db')
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM map_ban_onboarding_payment WHERE Account_Number = ? AND Vendor_Name = ?"
        cursor.execute(query, (account_number, vendor_name))
        row_count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return row_count > 0

    for index, row in df_csv.iterrows():
        account_number = row['account_number']
        vendor_name = row['vendor_name']
        
        if row_exists_in_database(account_number, vendor_name):
            df_csv.drop(index, inplace=True)

    dict_data = df_csv.to_dict(orient='records')
    for item in dict_data:
            keys = ', '.join(item.keys())
            values = ', '.join([f"'{value}'" for value in item.values()])
            cursor.execute(f"INSERT INTO map_ban_onboarding_payment ({keys}) VALUES ({values})")

    conn.commit()
    conn.close()

def process_csv_from_buffer():
    buffer_path = Path('buffer_csv_map.json')
    if buffer_path.exists():
        with open(buffer_path, 'r') as file:
            buffer_data_content = file.read()
            print("Buffer Data Content:",buffer_data_content)
            try:
                buffer_data = json.loads(buffer_data_content)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
                return
    else:
        buffer_data = []

    for data_entry in buffer_data:
        csv_path = data_entry.get('csv_path')
        process_csv_data(csv_path)

 

    if buffer_path.exists():
        buffer_path.unlink()


while True:
    print("working")
    process_csv_from_buffer()
    time.sleep(1)