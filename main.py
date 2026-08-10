import ui.startup as startup
import core.ai as ai

from database.database import DatabaseManager
from database.repository import (
    ConversationRepository,
    MessageRepository,
)
from services.conversation_service import ConversationService
from services.message_service import MessageService


database_manager = DatabaseManager()
database_manager.connect()

connection = database_manager.connection
if connection is None:
    raise RuntimeError("Database connection could not be established.")

conversation_repository = ConversationRepository(
    connection
)

message_repository = MessageRepository(
    connection
)

conversation_service = ConversationService(
    conversation_repository
)

message_service = MessageService(
    message_repository
)

ai.initialize_ai()

startup.start(
    conversation_service,
    message_service
)

database_manager.disconnect()