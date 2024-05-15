import os


def encode_filename(filename: str) -> str:
    return filename.encode('utf-8', 'ignore')


def rename_files(dir_path: str) -> None:
    files = os.listdir(dir_path)
    for name in files:
        base, ext = os.path.splitext(name)
        new_base = base.decode('utf-8')
        os.rename(
            os.path.join(dir_path, name),
            os.path.join(dir_path, new_base + ext)
        )


if __name__ == '__main__':
    dir_path = 'data/Šã¯ ¦¨ ¬ á« '
    rename_files(dir_path)
