def read_file(file_path: str) -> str:
    """Reads the file with given file path.

    Args:
        file_path (str): Path to the file that will be read.

    Returns:
        str: Content of the file.

    """
    file = open(file_path)
    content: str = file.read()
    file.close()
    return content
