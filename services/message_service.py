"""
Message service for Jarvis AI.
"""

from database.models.message import Message
from database.repository import MessageRepository

class MessageService:
    """
    Handles message-related application Logic.
    """

    def __init__(self, message_repository: MessageRepository) -> None:
        """
        Initializes the message service.
        """
        self.message_repository = message_repository

    def create_message(self, conversation_id: int, role: str, content: str) -> Message:
        """
        Creates a new message.
        """
        return self.message_repository.create_message(conversation_id, role, content)

    def get_message(self, message_id: int) -> Message | None:
        """
        Retrieves a message by its ID.
        """
        return self.message_repository.get_message(message_id)

    def get_all_messages(self) -> list[Message]:
        """
        Retrieves all messages.
        """
        return self.message_repository.get_all_messages()

    def get_messages_by_conversation(self, conversation_id: int) -> list[Message]:
        """
        Retrieves all messages for a specific conversation.
        """
        return self.message_repository.get_messages_by_conversation(conversation_id)

    def update_message(self, message_id: int, role: str, content: str) -> bool:
        """
        Updates a message's role and content.
        """
        return self.message_repository.update_message(message_id, content)

    def delete_message(self, message_id: int) -> bool:
        """
        Deletes a message by its ID.
        """
        return self.message_repository.delete_message(message_id)