import subprocess
import os
import urllib.parse

# List of links to process
links = [
    "https://github.com/obsidianmd/obsidian-help/tree/master/en/Linking%20notes%20and%20files",
    "https://github.com/obsidianmd/obsidian-help/tree/master/en/Files%20and%20folders",
    "https://github.com/obsidianmd/obsidian-help/tree/master/en/Plugins",
    "https://github.com/obsidianmd/obsidian-help/tree/master/en/Extending%20Obsidian",
    "https://github.com/obsidianmd/obsidian-help/tree/master/en/Obsidian%20Publish",
    "https://help.obsidian.md/Help+and+support"
]

for idx, link in enumerate(links):
    # Run onefilellm.py with the link as input
    subprocess.run(["python", "onefilellm.py", link], check=True)

    # Create a unique identifier based on the link
    parsed_url = urllib.parse.urlparse(link)
    path_parts = parsed_url.path.strip("/").split("/")
    identifier = "_".join(path_parts)

    # Ensure the identifier is not empty
    if not identifier:
        identifier = f"link_{idx+1}"

    # Rename compressed_output.txt
    if os.path.exists("compressed_output.txt"):
        new_compressed_name = f"compressed_output_{identifier}.txt"
        os.rename("compressed_output.txt", new_compressed_name)
        print(f"Renamed compressed_output.txt to {new_compressed_name}")

    # Rename uncompressed_output.txt
    if os.path.exists("uncompressed_output.txt"):
        new_uncompressed_name = f"uncompressed_output_{identifier}.txt"
        os.rename("uncompressed_output.txt", new_uncompressed_name)
        print(f"Renamed uncompressed_output.txt to {new_uncompressed_name}")
