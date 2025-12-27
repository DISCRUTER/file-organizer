import os
from pathlib import Path

DIRECTORIES = {
    "HTML" : [".html", ".htm", ".xhtml", ".html5"],
    "IMAGE" : [".jpeg", ".jpg", ".png", ".gif"],
    "VIDEO" : [".mp4", ".avi", ".mov", ".webm"],
    "DOCUMENTS" : [".epub", ".xls", ".xlsx", ".ppt", ".docx"],
    "AUDIO" : [".mp3", ".wav"],
    "PLAINTEXT" : [".txt"],
    "PDF" : [".pdf"],
    "PYTHON" : [".py"],
    "EXE" : [".exe"],
}

FILE_FORMATS = {file_format : directory for directory, file_formats in DIRECTORIES.items() for file_format in file_formats}

def organize_directory():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        
    for dir in os.scandir():
        try:
            os.rmdir(dir)
        except:
            pass

if __name__ == "__main__":
    organize_directory()