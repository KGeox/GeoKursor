import ctypes

def apply_cursor(path):
    Normal =32512
    new_cursor = ctypes.windll.user32.LoadCursorFromFileW(path)

    ctypes.windll.user32.SetSystemCursor(new_cursor, Normal)

# apply_cursor(r"C:\Users\HP\PycharmProjects\GeoKursor\data\cursorpacks\madaramangekyou\Arrow.ani")