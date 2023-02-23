import random
import pandas as pd
from tqdm import tqdm, trange
from pysus.online_data.SIH import download
from src.partos.data_load.states import load_states


def load_sih():
  # dfs = list()
  ufs = sorted([uf['sigla'] for uf in load_states()])
  pbar = tqdm(
    desc='Collect data from SIH',
    total=int(len(ufs)*10*12))
  meses = list(range(1, 12+1))
  anos = list(range(2010, 2020))
  # random.shuffle(meses)
  # random.shuffle(anos)
  # random.shuffle(ufs)
  for mes in meses:
    for ano in anos:
      for uf in ufs:
        data = download(uf, ano, mes)
        # dfs.append(data)
        pbar.update(1)
  pbar.close()
  # df = pd.concat(dfs)
  return True


def main():
  return load_sih()


__name__ == '__main__' and main()