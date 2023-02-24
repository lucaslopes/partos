from pathlib import Path


DB_PATH = f'{Path.home()}/Databases/partos/'
DB_PYSUS = f'{Path.home()}/pysus/'
DB_CITIES = DB_PATH + 'municipios'


# https://github.com/kelvins/Municipios-Brasileiros
URL_DB_CITIES = 'https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv'


# https://servicodados.ibge.gov.br/api/docs/
IBGE_STATES = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'


# PROCEDIMENTOS RELACIONADOS A INTERNAÇÃO PARA PARTO:
PARTOS = {
    '0310010039': 'NOR', # PARTO NORMAL
    '0310010047': 'NAR', # PARTO NORMAL EM GESTACAO DE ALTO RISCO
    '0310010055': 'NCT', # PARTO NORMAL EM CENTRO DE PARTO NORMAL
    '0310010012': 'NSD', # ASSISTÊNCIA AO PARTO SEM DISTOCIA
    '0411010034': 'CES', # PARTO CESARIANO
    '0411010026': 'CAR', # PARTO CESARIANO EM GESTACAO DE ALTO RISCO
    '0411010042': 'CLT', # PARTO CESARIANO C/ LAQUEADURA TUBARIA
}


# Especifique os filtros que você deseja aplicar a cada arquivo
FILTERS = [
    ("IDADE", ">=", 10),
    ("IDADE", "<=", 49),
    ("PROC_REA", 'in', '@'),
]


# Especifique as colunas que você deseja selecionar e os novos nomes das colunas
COLUMNS = {
    # 'DT_INTER': 'data',
    'PROC_REA': 'parto',
    'MUNIC_RES': 'origem',
    'MUNIC_MOV': 'destino',
    'CNES': 'cnes',
    'IDADE': 'idade',
}