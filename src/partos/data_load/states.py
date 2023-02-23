import json
import requests
from src.partos.config import IBGE_STATES
from src.partos.utils import save_local



def load_states(
        save: bool = True,
    ):
    req = requests.get(IBGE_STATES)
    states = json.loads(req.content.decode())
    if save:
        pass
        # save_local() # todo
    return states


def main():
  load_states()


__name__ == '__main__' and main()