"""
Database repositories for Jarvis AI.
"""

import sqlite3
from database.models.conversation import Conversation



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

    def get_conversation(self, conversation_id: int) -> Conversation | None:
        """
        Retrieves a conversation by its ID.
        """
        select_conversation_query = """
        SELECT *
        FROM conversations
        WHERE id = ?;
        """
        cursor = self.connection.execute(select_conversation_query, (conversation_id,))
        conversation_row = cursor.fetchone()
        if conversation_row is None:
            return None
        return Conversation(*conversation_row)

    def get_all_conversations(self) -> list[Conversation]:
        """
        Retrieves all conversations.
        """
        select_all_conversations_query = """
        SELECT *
        FROM conversations;
        """
        cursor = self.connection.execute(select_all_conversations_query)
        return [Conversation(*row) for row in cursor.fetchall()]

    def update_conversation(self, conversation_id: int, title: str) -> bool:
        """
        Updates a conversation's title.
        """
        update_conversation_query = """
        UPDATE conversations
        SET title = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?;
        """
        cursor = self.connection.execute(update_conversation_query, (title, conversation_id))
        self.connection.commit()
        return cursor.rowcount > 0

    def delete_conversation(self, conversation_id: int) -> bool:
        """
        Deletes a conversation by its ID.
        """
        delete_conversation_query = """
        DELETE FROM conversations
        WHERE id = ?;
        """
        cursor = self.connection.execute(delete_conversation_query, (conversation_id,))
        self.connection.commit()
        return cursor.rowcount > 0