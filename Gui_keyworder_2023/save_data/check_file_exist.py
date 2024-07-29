from pathlib import Path


def make_documents_subfolder(name):  # create folder "name" in User/Documents folder
    (Path.home() / "Documents" / f"{name}").mkdir(parents=True, exist_ok=True)
    return Path.home() / "Documents" / f"{name}"


def create_file_if_no(subfolder_name, file_name):
    path_to_folder = make_documents_subfolder(subfolder_name)
    Path(f'{path_to_folder}/{file_name}').touch(exist_ok=True)
    return f'{path_to_folder}/{file_name}'


if __name__ == '__main__':
    create_file_if_no('subfolder_name', 'file_name')
