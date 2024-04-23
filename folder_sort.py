import os
import shutil

def organize_files(source_folder):
    folder_mapping = {
        "jpg": "Images",
        "png": "Images",
        "gif": "Images",
        "pdf": "Documents",
        "docx": "Documents",
        "txt": "Documents",
        "mp3": "Music",
        "wav": "Music",
        "flac": "Music",
        "csv": "Data",
        "xlsx": "Data",
    }

    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            file_type = filename.split('.')[-1].lower()

            destination_folder = folder_mapping.get(file_type, "Other")
            destination_path = os.path.join(source_folder, destination_folder)

            os.makedirs(destination_path, exist_ok=True)

            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_path, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{destination_folder}'")

if __name__ == "__main__":
    folder_to_organize = "C:/data project"
    organize_files(folder_to_organize)



