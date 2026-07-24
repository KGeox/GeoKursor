
from pathlib import Path

def load_cursor_themes():
    base_dir = Path(__file__).parent.parent / 'data'/ 'cursorpacks'
    library_list = [pat.name for pat in base_dir.iterdir() if pat.is_dir()]
    return library_list

