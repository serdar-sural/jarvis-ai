"""
Application settings for Jarvis AI.

This module contains global configuration values
used throughout the application.
"""
from pathlib import Path

MODEL_NAME = "gpt-5.6-terra"
DATABASE_PATH = Path("data") / "jarvis.db"