import sys


def split_file(input_file, num_chunks, split_tag):
    """
    Splits the input text file into a specified number of chunks, ensuring splits occur after the previous occurrence of the specified tag.

    Args:
        input_file (str): The path to the input text file.
        num_chunks (int): The number of chunks to split the file into.
        split_tag (str): The tag or keyword to split the file at.

    Returns:
        None
    """
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_chunks
    chunks = []
    current_chunk = []
    last_split_index = 0

    for i, line in enumerate(lines):
        current_chunk.append(line)
        if len(current_chunk) >= chunk_size and split_tag in line:
            # Find the previous occurrence of the split_tag
            for j in range(i, last_split_index, -1):
                if split_tag in lines[j]:
                    chunks.append(lines[last_split_index : j + 1])
                    last_split_index = j + 1
                    current_chunk = []
                    break

    # Add any remaining lines to the last chunk
    if last_split_index < len(lines):
        chunks.append(lines[last_split_index:])

    # Ensure we have exactly num_chunks by merging smaller chunks if necessary
    while len(chunks) > num_chunks:
        chunks[-2].extend(chunks.pop())

    # If we have fewer chunks than required, split the largest chunk
    while len(chunks) < num_chunks:
        largest_chunk_index = max(range(len(chunks)), key=lambda i: len(chunks[i]))
        largest_chunk = chunks.pop(largest_chunk_index)
        mid_point = len(largest_chunk) // 2
        for j in range(mid_point, 0, -1):
            if split_tag in largest_chunk[j]:
                chunks.insert(largest_chunk_index, largest_chunk[: j + 1])
                chunks.insert(largest_chunk_index + 1, largest_chunk[j + 1 :])
                break

    for i, chunk in enumerate(chunks):
        output_file = f"{input_file.replace('.txt', '')}_part{i + 1}.txt"
        with open(output_file, "w", encoding="utf-8") as chunk_file:
            chunk_file.writelines(chunk)
        print(f"Written {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python split_file.py <input_file> <num_chunks> <split_tag>")
    else:
        input_file = sys.argv[1]
        num_chunks = int(sys.argv[2])
        split_tag = sys.argv[3]
        split_file(input_file, num_chunks, split_tag)
