import pandas as pd
from partos.utils import uf_ano_mes_iterator, get_path
from partos.config import (
    DB_PATH, DB_PYSUS,
    PARTOS, FILTERS, COLUMNS)
from partos.data_load import (
    load_states,
    download_sih,
    transform_sih)


df = pd.read_parquet(get_path('sih.parquet'))


df = transform_sih(
    iterator=uf_ano_mes_iterator(),
    # pysus_dir=DB_PYSUS,
    filters=FILTERS,
    columns=COLUMNS,
    partos=PARTOS)
df.to_parquet(f"{DB_PATH}sih.parquet")


# ufs = sorted([uf['sigla'] for uf in load_states()])
# download_sih(ufs)