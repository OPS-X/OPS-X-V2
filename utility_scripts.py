import os
import re

def rename_files(directory_path='.'):
    # List all files in the directory
    file_names = os.listdir(directory_path)

    # Filter out the .css files
    css_files = [file for file in file_names if file.endswith('.css')]

    # Regular expression pattern to find versioning
    pattern = re.compile(r'_V0\.(\d{2})\.css$')

    for file in css_files:
        match = pattern.search(file)
        if match:
            version_number = match.group(1)
            new_version = f"{int(version_number):03d}"
            new_file_name = pattern.sub(f'_{new_version}.css', file)
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_file_name))

def convert_filenames_to_constants(directory_path='.'):
    # List all files in the directory
    file_names = os.listdir(directory_path)

    # Filter out the .css files
    css_files = [file for file in file_names if file.endswith('.css')]

    # Remove the versioning and extensions from filenames
    formatted_files = [file.rsplit('_', 1)[0] for file in css_files]

    # Define the constant format
    const_format = "const cssFiles = [\n"
    const_format += ",\n".join([f'  "{name}"' for name in formatted_files])
    const_format += "\n];"

    return const_format

def main():
    while True:
        # Choose which function to run
        task = input("Enter 'rename' to rename files, 'convert' to generate constants, or 'exit' to quit: ").strip().lower()
        
        if task == 'rename':
            rename_files()
            print("Files renamed.")
        elif task == 'convert':
            constant_format_string = convert_filenames_to_constants()
            with open('css_constants.js', 'w') as file:
                file.write(constant_format_string)
            print("Output written to css_constants.js")
        elif task == 'exit':
            print("Exiting the script.")
            break
        else:
            print("Invalid task. Please enter 'rename', 'convert', or 'exit'.")

if __name__ == "__main__":
    main()
