import os
from pathlib import Path
from src.partos.config import DB_PATH


def make_path(db_path=DB_PATH):
    pth = ''
    paths = db_path.split('/')[1:-1]
    for p in paths:
        pth = f'{pth}/{p}'
        if not Path(pth).is_dir():
            print(f'Making dir: {pth}')
            os.mkdir(pth)
    return db_path


def get_path(fname):
    db_path = make_path()
    fpath = db_path + fname
    return fpath


def main():
    return get_path('')


__name__ == '__main__' and main()