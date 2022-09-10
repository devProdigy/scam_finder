from pathlib import Path

from dynaconf import LazySettings

env = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF=False,
    CORE_LOADERS_FOR_DYNACONF=["YAML"],
    MERGE_ENABLED_FOR_DYNACONF=True,
    load_dotenv=True,
)

# ---- LOG SECTION
LOGGER_NAME = "main_logger"
LOG_FILES_PATH = Path(__file__).parent / "logs"
LOGS_FILE_NAME_PATH = LOG_FILES_PATH / "log.txt"
Path(LOG_FILES_PATH).mkdir(parents=True, exist_ok=True)  # create folders if not exists
# ---- END of log section

# ---- Data path section
DATA_FOLDER_PATH = Path(__file__).parent / "text_data"
INPUT_DATA_FOLDER_PATH = DATA_FOLDER_PATH / "input"
OUTPUT_DATA_FOLDER_PATH = DATA_FOLDER_PATH / "output"
# ---- END of data path section
