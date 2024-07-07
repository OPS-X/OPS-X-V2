import os
import re

def increment_versions(directory_path='.'):
    file_names = os.listdir(directory_path)
    css_files = [file for file in file_names if file.endswith('.css')]
    pattern = re.compile(r'_(\d{3})\.css$')

    for file in css_files:
        match = pattern.search(file)
        if match:
            version_number = match.group(1)
            new_version = f"{int(version_number) + 1:03d}"
            new_file_name = pattern.sub(f'_{new_version}.css', file)
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_file_name))

def equalize_versions(directory_path='.'):
    file_names = os.listdir(directory_path)
    css_files = [file for file in file_names if file.endswith('.css')]
    pattern = re.compile(r'_(\d{3})\.css$')

    max_version = 0
    for file in css_files:
        match = pattern.search(file)
        if match:
            version_number = int(match.group(1))
            if version_number > max_version:
                max_version = version_number

    for file in css_files:
        match = pattern.search(file)
        if match:
            new_file_name = pattern.sub(f'_{max_version:03d}.css', file)
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_file_name))

def reset_versions(directory_path='.'):
    file_names = os.listdir(directory_path)
    css_files = [file for file in file_names if file.endswith('.css')]
    pattern = re.compile(r'_(\d{3})\.css$')

    for file in css_files:
        match = pattern.search(file)
        if match:
            new_file_name = pattern.sub('_001.css', file)
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_file_name))

def convert_filenames_to_constants(directory_path='.'):
    file_names = os.listdir(directory_path)
    css_files = [file for file in file_names if file.endswith('.css')]
    formatted_files = [file.rsplit('_', 1)[0] for file in css_files]

    const_format = "const cssFiles = [\n"
    const_format += ",\n".join([f'  "{name}"' for name in formatted_files])
    const_format += "\n];"

    return const_format

def main():
    while True:
        task = input("Enter 'increment' to increment versions, 'equalize' to set all to highest version, 'reset' to reset to 001, 'convert' to generate constants, or 'exit' to quit: ").strip().lower()
        
        if task == 'increment':
            increment_versions()
            print("Versions incremented.")
        elif task == 'equalize':
            equalize_versions()
            print("Versions equalized to highest.")
        elif task == 'reset':
            reset_versions()
            print("Versions reset to 001.")
        elif task == 'convert':
            constant_format_string = convert_filenames_to_constants()
            with open('css_constants.js', 'w') as file:
                file.write(constant_format_string)
            print("Output written to css_constants.js")
        elif task == 'exit':
            print("Exiting the script.")
            break
        else:
            print("Invalid task. Please enter 'increment', 'equalize', 'reset', 'convert', or 'exit'.")

if __name__ == "__main__":
    main()
