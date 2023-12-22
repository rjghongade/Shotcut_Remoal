import os

def remove_shortcut_virus(path):
    # Get a list of all files in the specified path
    files = os.listdir(path)

    for file_name in files:
        file_path = os.path.join(path, file_name)

        # Check if the file is a shortcut (extension .lnk)
        if file_name.endswith('.lnk') and os.path.isfile(file_path):
            try:
                # Delete the shortcut file
                os.remove(file_path)
                print(f"Deleted shortcut: {file_path}")
            except OSError as e:
                print(f"Error deleting shortcut: {file_path}")
                print(e)

        # If the file is a directory, recursively scan it
        elif os.path.isdir(file_path):
            remove_shortcut_virus(file_path)

# Specify the path to your USB drive
usb_drive_path = 'F:\\'  # Replace with the correct drive letter

remove_shortcut_virus(usb_drive_path)