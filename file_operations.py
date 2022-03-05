def read_file(file_path: str) -> str:
    file = open(file_path)
    content: str = file.read()
    file.close()
    return content
