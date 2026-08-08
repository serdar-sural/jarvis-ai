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

    def create_conversation(self, title: str) -> int:
        """
        Creates a new conversation.
        """
        insert_conversation_query = """
        INSERT INTO conversations (title) VALUES (?);
        """
        cursor = self.connection.execute(insert_conversation_query, (title,))
        self.connection.commit()

        conversation_id = cursor.lastrowid

        if conversation_id is None:
            raise RuntimeError("Failed to retrieve the last inserted conversation ID.")
        return conversation_id

    def get_conversation(self, conversation_id: int) -> tuple | None:
        """
        Retrieves a conversation by its ID.
        """
        select_conversation_query = """
        SELECT *
        FROM conversations
        WHERE id = ?;
        """
        cursor = self.connection.execute(select_conversation_query, (conversation_id,))
        return cursor.fetchone()

    def get_all_conversations(self) -> list[tuple]:
        """
        Retrieves all conversations.
        """
        select_all_conversations_query = """
        SELECT *
        FROM conversations;
        """
        cursor = self.connection.execute(select_all_conversations_query)
        return cursor.fetchall()