# this will read the log file and return the content as a string
from pathlib import Path
def read_log(file_path: str) -> str:
    path = Path(file_path) # cretating a path object from the file path

    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {file_path}")

    return path.read_text(encoding="utf-8")