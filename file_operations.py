# File operations
def read_file(file_path: str) -> str:
    """Reads the file with given file path.

    Args:
        file_path (str): Path to the file that will be read.

    Returns:
        str: Content of the file.

    """
    with open(file_path, "rb") as file:
        contents = file.read()
    file.close()

    return contents.decode("utf-8", "ignore")


def write_file(file_path: str, file_content: str):
    """Writes the content into the file.

    Args:
        file_path (str): Path to the file that will be written into.
        file_content (str): Content that will be written into file.

    """
    file = open(file_path, "w")
    file.write(file_content)
    file.close()


def get_file_name(file_path: str):
    """Gets the file name from provided file path

    Args:
        file_path (str): Path of the file.

    Returns:
        str: Name of the file.
    """
    return file_path.split('/')[-1]
