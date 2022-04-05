from random import randint
import tempfile


def temp_folder_with_files(file_data: str = "1", num_files: int = 3):
    """
    returns tempfile object folder with files that have data in them
    """
    if file_data == "random":
        file_data = str(randint(0, 10))
    temp_dir = tempfile.mkdtemp()
    temp_dir = Path(temp_dir)
    for i in range(num_files):
        temp_file = tempfile.mkstemp(dir=temp_dir, suffix=".txt")[1]
        with open(temp_file, "w") as file_handler:
            file_handler.write(file_data)
    return temp_dir
