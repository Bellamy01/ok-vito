import sqlite3

def add_ok_sign_column():
    try:
        conn = sqlite3.connect('customer_faces_data.db')
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE customers ADD COLUMN ok_sign_detected INTEGER DEFAULT 0")
        conn.commit()
        print("Column 'ok_sign_detected' added successfully.")
    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")

if __name__ == '__main__':
    # add when first running it
    add_ok_sign_column()
