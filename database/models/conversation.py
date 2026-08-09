"""
Conversation model for Jarvis AI.
"""

from dataclasses import dataclass

@dataclass
class Conversation:
    id: int
    title: str
    created_at: str
    updated_at: str