import os

# HTTP Basic Auth
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

# Database access
DB_HOST = os.environ.get("DB_HOST")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_DRIVER_NAME = "postgresql+psycopg2"
