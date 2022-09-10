import inject

from app.dependencies import inject_config
from app.logger import setup_logging
from app.run_app import run_finder


if __name__ == "__main__":
    setup_logging()

    # inject dependencies for the future insert and reuse.
    inject.configure_once(inject_config, bind_in_runtime=False)

    run_finder()
