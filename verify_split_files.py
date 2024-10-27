import sys


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def verify_split_files(original_file, split_files):
    """
    Verifies that the combined content of the split files matches the original file.

    Args:
        original_file (str): The path to the original text file.
        split_files (list of str): The paths to the split text files.

    Returns:
        None
    """
    original_content = read_file(original_file)
    combined_content = "".join(read_file(file) for file in split_files)

    if original_content == combined_content:
        print(
            "Verification successful: All split files contain the complete content of the original file."
        )
    else:
        print(
            "Verification failed: The content of the split files does not match the original file."
        )
        print(f"Original content length: {len(original_content)}")
        print(f"Combined content length: {len(combined_content)}")
        # Debugging: Print the first few characters of each content to identify discrepancies
        print(f"Original content start: {original_content[:100]}")
        print(f"Combined content start: {combined_content[:100]}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python verify_split_files.py <original_file> <split_file1> <split_file2> ... <split_fileN>"
        )
    else:
        original_file = sys.argv[1]
        split_files = sys.argv[2:]
        verify_split_files(original_file, split_files)
