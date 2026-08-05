"""
Database management for Jarvis AI.

This module contains the DatabaseManager class, which is responsible for managing
the application's database connection.
"""

import sqlite3
import config.settings as settings
from core.logger import logger


class DatabaseManager:
    """
    Manages the application's database connection.
    """

    def __init__(self) -> None:
        self.database_path = settings.DATABASE_PATH
        self.connection = None

        self._create_data_directory()

    def connect(self) -> None:
        """
        Establishes a connection to the application's database.
        """

        if self.connection is not None:
            logger.warning("Database connection already established.")
            return

        try:
            self.connection = sqlite3.connect(self.database_path)
            logger.info("Database connection established.")
        except sqlite3.Error as error:
            logger.error(f"Failed to connect to database {self.database_path}: {error}")
            raise

    def _create_data_directory(self) -> None:
        """
        Creates the data directory if it does not already exist.
        """

        data_directory = self.database_path.parent

        if not data_directory.exists():
            data_directory.mkdir(parents=True, exist_ok=True)
            logger.info("Created data directory.")

    def disconnect(self) -> None:
        """
        Closes the connection to the application's database.
        """

        if self.connection is None:
            logger.warning("No database connection to close.")
            return

        try:
            self.connection.close()
            self.connection = None
            logger.info("Database connection closed.")
        except sqlite3.Error as error:
            logger.error(f"Failed to close database connection {self.database_path}: {error}")
            raise