"""
Message model for Jarvis AI.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Message:
    """
    Represents a message in a conversation.
    """

    id: int
    conversation_id: int
    role: str
    content: str
    created_at: datetime
    updated_at: datetime