import os
import sqlite3
import pandas as pd
from flask import Flask
from flask_caching import Cache
from app.routes import register_routes
from app.config import DB_PATH

def create_db_from_csv(csv_path, db_path, table_name):
    """
    Convert a CSV file into an SQLite database.

    Args:
        csv_path (str): The path to the CSV file.
        db_path (str): The path to the SQLite database file.
        table_name (str): The name of the table to create in the database.
    """
    # Load the CSV into a DataFrame
    df = pd.read_csv(csv_path)
    # Create or connect to the SQLite database
    with sqlite3.connect(db_path) as conn:
        # Write the DataFrame to a new SQLite table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        # Add an index on the playerID column to optimize queries
        cursor = conn.cursor()
        query = (
            f"CREATE INDEX IF NOT EXISTS idx_playerID "
            f"ON {table_name} (playerID)"
        )
        cursor.execute(query)
        conn.commit()
        # Close the cursor
        cursor.close()

def create_app():
    """
    Function to create and configure a Flask application.
    
    Returns:
        Flask: A Flask application instance.
    """
    app = Flask(__name__)
    # Configure caching
    cache = Cache(
        config={
            'CACHE_TYPE': 'flask_caching.backends.simplecache.SimpleCache'
        }
    )
    cache.init_app(app)
    # Create SQLite database from CSV file
    create_db_from_csv(
        csv_path='./data/Player.csv', 
        db_path=DB_PATH, 
        table_name='players'
    )
    # Register all routes for the REST API
    register_routes(app, cache)
    return app

if __name__ == '__main__':
    # Create an application instance and run the development server.
    app = create_app()
    # Start Flask development server that listens on all network interfaces.
    app.run(host='0.0.0.0', port=5001, debug=True)