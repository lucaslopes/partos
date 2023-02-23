import pandas as pd
from datetime import datetime
from src.partos.utils.paths import get_path


def save_local(
        df: pd.DataFrame,
        fpath: str,
    ):
    # compressions = ['bz2', 'xz', 'zip']
    # for compr in compressions:
    # file_path = f'{fpath}.csv.{compr}'
    file_path = f'{fpath}'
    begin = datetime.now()
    df.to_parquet(file_path, index=False)
    # df.to_csv(
    #     file_path,
    #     index=False,
    #     compression=compr)
    dur = datetime.now() - begin
    print(f'parquet dump -> {dur}')
    begin = datetime.now()
    df_temp = pd.read_parquet(file_path)
    dur = datetime.now() - begin
    print(f'parquet read -> {dur}')
    # parquet dump -> 0:00:00.007277
    # parquet read -> 0:00:00.012887


def main():
    return None # save_local()


__name__ == '__main__' and main()