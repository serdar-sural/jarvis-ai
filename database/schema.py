"""
Database schema for Jarvis AI.

This module contains functions for creating and managing
the application's database schema.
"""

import sqlite3

def create_tables(connection: sqlite3.Connection) -> None:
    """
    Creates all required database tables.
    """

    create_conversations_table(connection)
    create_messages_table(connection)

def create_conversations_table(connection: sqlite3.Connection) -> None:
    """
    Creates the conversations table.
    """

    create_table_query = """
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """
    connection.execute(create_table_query)
    connection.commit()

def create_messages_table(connection: sqlite3.Connection) -> None:
    """
    Creates the messages table.
    """
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        conversation_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conversation_id) REFERENCES conversations (id) ON DELETE CASCADE
    );
    """
    connection.execute(create_table_query)
    connection.commit()