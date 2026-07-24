
from pathlib import Path

def load_cursor_themes():

    base_dir = Path(__file__).parent.parent / 'data'/ 'cursorpacks'
    if base_dir.exists():
        library_list = [pat.name for pat in base_dir.iterdir() if pat.is_dir()]
        return library_list

def load_theme(name):
    base_dir = Path(__file__).parent.parent / 'data' / 'cursorpacks' / name

    themes = [cur.name for cur in base_dir.iterdir() if cur.is_file()]
    print(themes)
    return themes
