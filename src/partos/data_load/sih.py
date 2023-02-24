import os
import pandas as pd
from itertools import product
import pyarrow.parquet as pq
from tqdm import tqdm
from pysus.online_data.SIH import download


def download_sih(
    iterator
  ):
  # Once every file was downloaded:
  # Collecting SIH data: 100%|█████████████████| 3240/3240 [02:09<00:00, 25.06it/s]
  pbar = tqdm(
    desc='Collecting SIH data',
    total=27*10*12)
  for uf, ano, mes in iterator:
    download(uf, ano, mes)
    pbar.update(1)
  pbar.close()
  return True


def transform_sih(
    iterator,
    filters,
    columns,
    partos,
  ):
  # 100%|███████████| 3240/3240 [24:57<00:00,  2.16it/s]
  result = pd.DataFrame()
  pbar = tqdm(
    desc='Collecting SIH data',
    total=27*10*12)
  for uf, ano, mes in iterator:
    df = download(uf, ano, mes)
    for col, op, val in filters:
      if op == 'in':
        partos_list = list(partos)
        val = '@partos_list'
      df = df.query(f"{col} {op} {val}")
    df = df.loc[
      :, list(columns.keys())
    ].rename(columns=columns)
    df['parto'].replace(partos, inplace=True)
    df['uf'] = uf
    df['ano'] = ano
    df['mes'] = mes
    result = pd.concat([result, df])
    pbar.update(1)
  pbar.close()
  return result

# files = [
#   f for f in os.listdir(pysus_dir)
#     if f.endswith(".parquet")]
# for filename in tqdm(files):
#   file_path = os.path.join(pysus_dir, filename)
#   df = pd.read_parquet(file_path)


def main():
    return True


__name__ == '__main__' and main()