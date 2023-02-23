from pathlib import Path


DB_PATH = f'{Path.home()}/Databases/partos/'
DB_PYSUS = f'{Path.home()}/pysus/'
DB_CITIES = DB_PATH + 'municipios'


# https://github.com/kelvins/Municipios-Brasileiros
URL_DB_CITIES = 'https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv'


# https://servicodados.ibge.gov.br/api/docs/
IBGE_STATES = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'