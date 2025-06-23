import pathlib
import zipfile

def make_archive(filepaths, destin_dir):
    destin_path = pathlib.Path(destin_dir, "compressed.zip")
    with zipfile.ZipFile(destin_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["test1.txt", "test2.txt"], destin_dir=r"D:\Projects\Python\Bonus")