import os

def scan_empty_folders(drive):
    empty_folders = []
    for root, dirs, files in os.walk(drive):
        if not dirs and not files:
            empty_folders.append(root)
    return empty_folders
