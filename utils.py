import logging
import sys
import pandas as pd
from typing import Any, Optional

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("Scheduler")
    if not logger.handlers:
        fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%M:%S')
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(fmt)
        logger.addHandler(sh)
    logger.setLevel(logging.INFO)
    return logger

def log_section(logger: logging.Logger, title: str, content: Any) -> None:
    logger.info(f"=== {title} ===")
    print(content)
    print("-" * 40)

def load_csv(file_path: str, sep: str | None=None) -> pd.DataFrame:
    """Carga robusta de CSV."""
    try:
        if sep is None:
            return pd.read_csv(file_path, sep=',')
        else:
            return pd.read_csv(file_path, sep=sep)
    except Exception as e:
        logging.error(f"Error al cargar el archivo {file_path}: {e}")
        raise
