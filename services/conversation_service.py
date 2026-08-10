"""
Conversation service for Jarvis AI.
"""

from database.models.conversation import Conversation
from database.repository import ConversationRepository


class ConversationService:
    """
    Handles conversation-related application Logic.
    """
    def __init__(self, conversation_repository: ConversationRepository) -> None:
        """
        Initializes the conversation service.
        """
        self.conversation_repository = conversation_repository

    def create_conversation(self, title: str) -> Conversation:
        """
        Creates a new conversation.
        """
        return self.conversation_repository.create_conversation(title)

    def get_conversation(self, conversation_id: int) -> Conversation| None:
        """
        Retrieves a conversation by its ID.
        """
        return self.conversation_repository.get_conversation(conversation_id)

    def get_all_conversations(self) -> list[Conversation]:
        """
        Retrieves all conversations.
        """
        return self.conversation_repository.get_all_conversations()

    def update_conversation(self, conversation_id: int, title: str) -> bool:
        """
        Updates a conversation's title.
        """
        return self.conversation_repository.update_conversation(conversation_id, title)

    def delete_conversation(self, conversation_id: int) -> bool:
        """
        Deletes a conversation by its ID.
        """
        return self.conversation_repository.delete_conversation(conversation_id)