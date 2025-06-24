import pathlib
import zipfile

def extract_archive(archive_path, destin_dir):
    with zipfile.ZipFile(archive_path, "r") as archive_file:
        archive_file.extractall(destin_dir)

if __name__ == "__main__":
    extract_archive(archive_path="compressed.zip", destin_dir=r"D:\Projects\Python\Bonus")