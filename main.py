import ui.startup as startup
import core.ai as ai

from database.database import DatabaseManager


database_manager = DatabaseManager()
database_manager.connect()

ai.initialize_ai()
startup.start()

database_manager.disconnect()