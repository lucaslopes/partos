import sys
pth = '/'.join(__file__.split('/')[:-3])
sys.path.append(pth)

import os
import pandas as pd
import datatable as dt
import pyarrow.parquet as pq
from tqdm import tqdm
from partos.config import (
    DB_PATH, DB_PYSUS,
    PARTOS, FILTERS, COLUMNS)


def transform_sih_old(
        pysus_dir=DB_PYSUS,
        output_path=DB_PATH,
        columns=COLUMNS,
        filters=FILTERS,
        partos=PARTOS,
    ):

    # Crie um dataframe vazio para armazenar os dados processados
    result = pd.DataFrame()

    # Percorra cada arquivo *.parquet no diretório e aplique as transformações
    files = os.listdir(pysus_dir)
    for filename in tqdm(files):
        if filename.endswith(".parquet"):
            file_path = os.path.join(pysus_dir, filename)
            table = pq.read_table(file_path)
            df = table.to_pandas()
            
            # Aplique os filtros
            for col, op, val in filters:
                df = df.query(f"{col} {op} {val}")
            
            # Selecione as colunas e renomeie-as
            df = df.loc[:, list(columns.keys())].rename(columns=columns)

            # Renomeie os tipos de partos
            df['parto'].replace(partos, inplace=True)
            
            # Adicione os dados processados ao dataframe resultante
            result = pd.concat([result, df])

    # Agrupe as colunas e some os procedimentos
    result['procedimentos'] = 1
    result = result.groupby(list(columns.values()), as_index=False).sum()


    # Salve o dataframe resultante em um novo arquivo *.parquet
    result.to_parquet(f"{output_path}sih.parquet")
    
    return result


def load_sih_prq_jay(output_path=DB_PATH):
    pth_prq = f"{output_path}sih.parquet"
    pth_jay = f"{output_path}sih.jay"
    df_prq = pd.read_parquet(pth_prq)
    df_jay = dt.fread(pth_jay).to_pandas()
    df_jay.drop(columns=['ano', 'cnes'], inplace=True)
    df_jay = df_jay.groupby(list(df_jay.columns)[:-1], as_index=False).sum()
    df_jay.rename(columns={'procedimento': 'parto', 'count': 'procedimentos'}, inplace=True)
    df_jay['parto'] = df_jay['parto'].apply(lambda x: f'0{x}')
    df_jay['parto'] = df_jay['parto'].replace(PARTOS)
    df_prq[['origem', 'destino']] = df_prq[['origem', 'destino']].astype(int)
    df = pd.merge(
        left=df_prq,
        right=df_jay,
        how='outer',
        on=['origem', 'destino', 'parto'],
        suffixes=['_prq', '_jay'])
    df['diff'] = df['procedimentos_prq'] - df['procedimentos_jay']
    # return df_prq, df_jay
    return df


def main():
    return None
    df = transform_sih()


__name__ == '__main__' and main()