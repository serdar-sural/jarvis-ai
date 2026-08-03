from datetime import datetime
from pathlib import Path


LOG_FILE_PATH = Path(__file__).parent.parent / "logs" / "app.log"


class Logger:
    def __init__(self):
        self._create_log_directory()

    def _create_log_directory(self):
        LOG_FILE_PATH.parent.mkdir(exist_ok=True)

    def info(self, message):
        self._write_log("INFO", message)

    def warning(self, message):
        self._write_log("WARNING", message)

    def error(self, message):
        self._write_log("ERROR", message)

    def debug(self, message):
        self._write_log("DEBUG", message)

    def _write_log(self, level, message):
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {level}: {message}\n")


logger = Logger()