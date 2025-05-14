class DatabaseNotConfigured(Exception):
    """
    Exception raised when the database is not configured.
    """

    def __init__(self, message="Database is not configured. Check your database connection settings."):
        super().__init__(message)
        self.message = message
