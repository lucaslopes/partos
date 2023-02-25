import sys
from pathlib import Path
path = f'{Path.home()}/Code/partos/src'
sys.path.append(path)

import pandas as pd
import plotly.express as px
import streamlit as st

from partos import config


@st.cache_data
def load_data(path):
    return pd.read_parquet(path)


@st.cache_data
def group_df(
        df: pd.DataFrame
    ):
    cols = ['ano', 'mes', 'parto']
    df_ = df[cols].copy()
    df_['procedimentos'] = 1
    df_ = df_.groupby(cols, as_index=False).sum()
    df_['ano'] = df_['ano'].astype(str)
    df_['mes'] = df_['mes'].apply(lambda x: f"{x:02d}")
    df_['data'] = df_['ano'] + '-' + df_['mes']
    df_['data'] = pd.to_datetime(df_['data'])
    df_.drop(columns=cols[:-1], inplace=True)
    return df_

st.header('Introdução')

path1 = f'{config.DB_PATH}sih.parquet'
path2 = f'{config.DB_PATH}sih_pcdas.parquet'
for pth in [path1, path2]:
    df = load_data(pth)
    df_ = group_df(df)
    fig = px.scatter(df_, x='data', y='procedimentos', color='parto', trendline='ols')
    st.plotly_chart(fig)