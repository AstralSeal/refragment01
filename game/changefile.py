import os

# Specify the directory containing the files
directory = "D:/renpy-8.0.3-sdk/renpy-8.0.3-sdk/project3rd/game/images/Sprite/yuno01"

# Get a list of all files in the directory
files = os.listdir(directory)

# Filter files that start with "shoko"
shoko_files = [file for file in files if file.startswith("nanami")]

# Rename each file
for file in shoko_files:
    # Create the new file name by replacing 'shoko' with 'maya'
    new_name = file.replace("nanami", "yuno", 1)
    # Construct the full file path
    old_path = os.path.join(directory, file)
    new_path = os.path.join(directory, new_name)
    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed '{file}' to '{new_name}'")

print("All files renamed successfully.")