def write_file(file_name, file_content):
    """Write content to a new .txt file"""
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to an existing .txt file"""
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as file:
        file.write(eppend_content)

def read_file(file_name):
    """Read and return content from a .txt file"""
    with open(f"{file_name}.txt", mode="r", encoding="utf-8") as file:
        return file.read()
