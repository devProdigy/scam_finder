import traceback
from logging.config import dictConfig
from pathlib import Path

from colorlog import ColoredFormatter

import settings

__all__ = ["setup_logging"]

LOGS_TO_SUPPRESS = tuple()
ROOT = Path(__file__).parent.parent
TRACEBACK_ANALYSE_LIMIT = 20


class LogFormatter(ColoredFormatter):
    """Formatter that adds extra logging info."""

    @staticmethod
    def _extract_exc_location(exc_tb):
        """Lookup traceback for the lowest line of source code.

        Provide extra context if a line is found within the limit.
        """
        local_code_frame = None
        local_code_path = None

        for frame in traceback.extract_tb(exc_tb, limit=TRACEBACK_ANALYSE_LIMIT):
            frame_path = Path(frame.filename)
            if ROOT not in frame_path.parents:
                break
            local_code_frame, local_code_path = frame, frame_path

        if not local_code_frame:
            return {}

        module = local_code_path.relative_to(ROOT)
        return {
            "location": ".".join(module.parts[:-1] + (module.stem, local_code_frame.name)),
            "line": repr(local_code_frame.line),
        }


def setup_logging(name: str = settings.LOGGER_NAME, full_log_file_name: str = settings.LOGS_FILE_NAME_PATH):
    """Set up the logging."""
    log_level = "INFO"
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": LogFormatter,
                "fmt": f"%(log_color)s %(asctime)s %(levelname)s [%(name)s] %(message)s %(reset)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red",
                },
            }
        },
        "handlers": {
            "default": {"class": "logging.StreamHandler", "level": log_level, "formatter": "default"},
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": log_level,
                "formatter": "default",
                "filename": full_log_file_name,
                "encoding": "utf-8",
                "backupCount": settings.env.BACKUP_LOGS_AMOUNT,
                "interval": settings.env.DAYS_TILL_NEW_LOG_FILE,
                "when": "midnight",
            },
        },
        "loggers": {name: {"level": log_level}, **{k: {"level": "WARNING"} for k in LOGS_TO_SUPPRESS}},
        "root": {"level": log_level, "handlers": ["default", "file"]},
    }
    dictConfig(config)
