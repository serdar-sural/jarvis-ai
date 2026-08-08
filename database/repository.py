"""
Database repositories for Jarvis AI.
"""

import sqlite3




class ConversationRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        """
        Initializes the repository with a database connection.
        """
        self.connection = connection

    def create_conversation(self, title: str) -> None:
        """
        Creates a new conversation.
        """
        insert_conversation_query = """
        INSERT INTO conversations (title) VALUES (?);
        """
        self.connection.execute(insert_conversation_query, (title,))
        self.connection.commit()
            