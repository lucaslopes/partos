import os
from pathlib import Path
from partos.config import DB_PATH
import pandas as pd
from itertools import product


def save_local(
        df: pd.DataFrame,
        fpath: str,
    ):
    file_path = f'{fpath}'
    df.to_parquet(file_path, index=False)
    return True


def uf_ano_mes_iterator():
    ufs = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    anos = range(2010, 2020)
    meses = range(1, 13)
    iterator = product(ufs, anos, meses)
    return iterator


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