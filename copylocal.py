import os


def list_files_and_contents(root_dir, max_depth=4, current_depth=1, output_file=None):
    """Recursively lists .tsx, .py, and .env files and their contents in a directory up to a specified depth."""
    if current_depth > max_depth or not os.path.exists(root_dir):
        return

    try:
        with os.scandir(root_dir) as it:
            for entry in it:
                if entry.is_dir():
                    list_files_and_contents(
                        entry.path, max_depth, current_depth + 1, output_file
                    )
                elif entry.name.endswith((".tsx", ".py", ".env", ".j2")):
                    output_file.write(f"{entry.name}\n")
                    try:
                        with open(entry.path, "r", encoding="utf-8") as file:
                            content = file.read()
                            output_file.write(f"Contents:\n{content}\n\n")
                    except UnicodeDecodeError:
                        output_file.write(
                            "Contents: [Binary or non-text content, not displayed]\n\n"
                        )
    except PermissionError:
        output_file.write(f"{entry.name}/ (Permission Denied)\n")


# Set the root directory to the desired path. Ensure this path exists.
root_directory = "/Users/npatel/Documents/Dev/ankibyte/"

# Open a file to save the output
with open("content.txt", "w", encoding="utf-8") as output_file:
    # Call the function to list files and their contents, passing the output file
    list_files_and_contents(root_directory, output_file=output_file)
