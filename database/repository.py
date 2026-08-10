"""
Database repositories for Jarvis AI.
"""

import sqlite3
from datetime import datetime

from database.models.conversation import Conversation
from database.models.message import Message


class ConversationRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        """
        Initializes the repository with a database connection.
        """
        self.connection = connection

    def create_conversation(self, title: str) -> Conversation:
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

        conversation = self.get_conversation(conversation_id)
        if conversation is None:
            raise RuntimeError("Failed to retrieve the newly created conversation.")
        return conversation

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
        return self._row_to_conversation(conversation_row)

    def get_all_conversations(self) -> list[Conversation]:
        """
        Retrieves all conversations.
        """
        select_all_conversations_query = """
        SELECT *
        FROM conversations;
        """
        cursor = self.connection.execute(select_all_conversations_query)
        return [
            self._row_to_conversation(row)
            for row in cursor.fetchall()
        ]  

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

    def _row_to_conversation(self, row: tuple) -> Conversation:
        """
        Converts a database row to a Conversation object.
        """
        return Conversation(
            id=row[0],
            title=row[1],
            created_at=datetime.fromisoformat(row[2]),
            updated_at=datetime.fromisoformat(row[3])
        )


class MessageRepository:

    def __init__(self, connection: sqlite3.Connection) -> None:
        """
        Initializes the repository with a database connection.
        """
        self.connection = connection

    def create_message(
        self,
        conversation_id: int,
        role: str,
        content: str
    ) -> Message:
        """
        Creates a new message.
        """
        insert_message_query = """
        INSERT INTO messages (conversation_id, role, content)
        VALUES (?, ?, ?);
        """

        cursor = self.connection.execute(
            insert_message_query,
            (conversation_id, role, content)
        )
        self.connection.commit()

        message_id = cursor.lastrowid

        if message_id is None:
            raise RuntimeError(
                "Failed to retrieve the last inserted message ID."
            )
        message = self.get_message(message_id)
        if message is None:
            raise RuntimeError(
                "Failed to retrieve the newly created message."
            )
        return message

    def get_message(self, message_id: int) -> Message | None:
        """
        Retrieves a message by its ID.
        """

        select_message_query = """
        SELECT *
        FROM messages
        WHERE id = ?;
        """

        cursor = self.connection.execute(
            select_message_query,
            (message_id,)
        )

        message_row = cursor.fetchone()

        if message_row is None:
            return None

        return self._row_to_message(message_row)

    def _row_to_message(self, row: tuple) -> Message:
        """
        Converts a database row to a Message object.
        """

        return Message(
            id=row[0],
            conversation_id=row[1],
            role=row[2],
            content=row[3],
            created_at=datetime.fromisoformat(row[4]),
            updated_at=datetime.fromisoformat(row[5])
        )


    def get_all_messages(self) -> list[Message]:
        """
        Retrieves all messages.
        """

        select_all_messages_query = """
        SELECT *
        FROM messages
        ORDER BY created_at ASC;
        """

        cursor = self.connection.execute(select_all_messages_query)

        return [
            self._row_to_message(row)
            for row in cursor.fetchall()
        ]

    def get_messages_by_conversation(self, conversation_id: int) -> list[Message]:
        """
        Retrieves all messages for a specific conversation.
        """

        select_messages_by_conversation_query = """
        SELECT *
        FROM messages
        WHERE conversation_id = ?
        ORDER BY created_at ASC;
        """

        cursor = self.connection.execute(
            select_messages_by_conversation_query,
            (conversation_id,)
        )

        return [
            self._row_to_message(row)
            for row in cursor.fetchall()
        ]

    def update_message(self, message_id: int, content: str) -> bool:
        """
        Updates a message's content.
        """

        update_message_query = """
        UPDATE messages
        SET content = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?;
        """

        cursor = self.connection.execute(
            update_message_query,
            (content, message_id)
        )
        self.connection.commit()

        return cursor.rowcount > 0

    def delete_message(self, message_id: int) -> bool:
        """
        Deletes a message by its ID.
        """

        delete_message_query = """
        DELETE FROM messages
        WHERE id = ?;
        """

        cursor = self.connection.execute(
            delete_message_query,
            (message_id,)
        )
        self.connection.commit()

        return cursor.rowcount > 0
