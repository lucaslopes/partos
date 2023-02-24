from datetime import datetime
import pandas as pd
from partos.config import URL_DB_CITIES, DB_CITIES
from partos.utils import save_local


def load_cities(
        url_cities: str = URL_DB_CITIES,
        save: bool = True,
        save_path: str = DB_CITIES,
    ):
    # save_path = save_path + '.csv.zip' if (
    #     'csv' not in save_path
    # ) else save_path
    # try:
    #     df = pd.read_csv(save_path)
    # except:
    df = pd.read_csv(url_cities)
    if save: save_local(df, save_path)
    return df


def main():
    return load_cities()


__name__ == '__main__' and main()