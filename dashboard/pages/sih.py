import sys
pth = '/'.join(__file__.split('/')[:-3])
sys.path.append(pth)

import plotly.express as px
import streamlit as st
from src.partos.data_transform import load_sih_prq_jay

df = load_sih_prq_jay()

st.dataframe(df)

fig = px.scatter(
    df,
    x='procedimentos_prq',
    y='procedimentos_jay',
    # size=abs(df['diff'])
)

st.plotly_chart(fig)

fig_hist = px.histogram(df['diff'])
st.plotly_chart(fig_hist)