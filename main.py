import ui.startup as startup
import core.ai as ai
from database.database import DatabaseManager 

database_manager = DatabaseManager()
database_manager.connect()
database_manager.disconnect()

ai.initialize_ai()
startup.start()

