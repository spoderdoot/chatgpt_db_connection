import sqlite3

def get_metadata_from_db():
    # Setup a connection to the local database and create an object which can execute SQL queries
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    metadata = {}
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        table_metadata = cursor.fetchall()
        metadata[table] = table_metadata

    return {'metadata': metadata}

def post_sql_query_to_db(sqlQuery: str):
    # Setup a connection to the local database and create an object which can execute SQL queries
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()

    cursor.execute(sqlQuery)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    return {'result': data}, 200