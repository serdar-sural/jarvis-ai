"""
Conversation model for Jarvis AI.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Conversation:
    id: int
    title: str
    created_at: datetime
    updated_at: datetime