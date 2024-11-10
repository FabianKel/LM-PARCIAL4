from config_loader import load_config
from turing_machine import TuringMachine
from simulator import Simulator
from pprint import pprint

if __name__ == "__main__":
    config = load_config("config.yaml")
    #config = load_config("configReject.yaml")
    #config = load_config("configAccept.yaml")
    #config = load_config("configLoop.yaml")


    key_replacements = {
    'Î£': 'Σ',
    'Î“': 'Γ',
    'Î´': 'δ'
    }
    for old_key, new_key in key_replacements.items():
        if old_key in config:
            config[new_key] = config.pop(old_key)
    pprint(config, width=80, sort_dicts=False)

    tm = TuringMachine(config)
    simulator = Simulator(tm)

    cadena = config["cadena"]
    if not cadena:
        cadena = input("Ingrese una cadena para la simulación: ")
    result = simulator.simulate(cadena)
    print(f"Resultado: {result}")
