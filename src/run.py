import zipfile
import datatable as dt
import pandas as pd
from tqdm import tqdm
from partos.utils import uf_ano_mes_iterator, get_path
from partos.config import (
  DB_PATH, DB_PYSUS,
  PARTOS, FILTERS, COLUMNS)
from partos.data_load import (
  load_states,
  download_sih,
  transform_sih,
  transform)


columns = {
  'PROC_REA': 'parto',
  'res_codigo_adotado': 'origem',
  'int_codigo_adotado': 'destino',
  'CNES': 'cnes',
  'IDADE': 'idade',
  'ANO_CMPT': 'ano',
  'MES_CMPT': 'mes',
  'int_SIGLA_UF': 'uf',
}


def load_sih_pcdas():
  result = pd.DataFrame()
  pth = get_path('SIHSUS.zip')
  with zipfile.ZipFile(pth) as myzip:
    files = [
      f for f in myzip.namelist()
        if f.endswith('.csv') and 'dict' not in f]
    for file in tqdm(files):
      with myzip.open(file) as myfile:
        # df = dt.fread(myfile).to_pandas()
        df = pd.read_csv(myfile, low_memory=False)
        df['PROC_REA'] = df['PROC_REA'].apply(lambda x: f'0{x}')
        df = transform(df, FILTERS, columns, PARTOS)
        df = df[(df['ano'] >= 2010) & (df['ano'] < 2020)]
        result = pd.concat([result, df])
    return result


df = load_sih_pcdas()
df.to_parquet(get_path('sih_pcdas_dt.parquet'), index=False)


# df = pd.read_parquet(get_path('sih.parquet'))
# df = transform_sih(
#   iterator=uf_ano_mes_iterator(),
#   # pysus_dir=DB_PYSUS,
#   filters=FILTERS,
#   columns=COLUMNS,
#   partos=PARTOS)
# df.to_parquet(f"{DB_PATH}sih.parquet")


# ufs = sorted([uf['sigla'] for uf in load_states()])
# download_sih(ufs)