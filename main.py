from config_loader import load_config
from turing_machine import TuringMachine
from simulator import Simulator
from pprint import pprint

if __name__ == "__main__":
    config_files = [
        ("configAccept.yaml", "simulation_output_accept.txt"),
        ("configReject.yaml", "simulation_output_reject.txt"),
        ("configLoop.yaml", "simulation_output_loop.txt"),
        #Configuracion para las maquinas de ejemplos adicionales
        #("config.yaml", "simulation_testing.txt")
    ]
    
    key_replacements = {
        'Î£': 'Σ',
        'Î“': 'Γ',
        'Î´': 'δ'
    }

    for config_file, output_file in config_files:
        print(f"\nSimulating with configuration: {config_file}")
        
        # Cargar la configuración y reemplazar los símbolos leidos incorrectamente
        config = load_config(config_file)
        for old_key, new_key in key_replacements.items():
            if old_key in config:
                config[new_key] = config.pop(old_key)
        
        # Instancia la Máquina y el simulador con la configuración
        tm = TuringMachine(config)
        simulator = Simulator(tm)

        cadena = config.get("cadena", "")
        if not cadena:
            cadena = input("Ingrese una cadena para la simulación: ")
        
        # Ejecutar la simulación y guardar el resultado en un archivo .txt
        if config.get("description", "") != "":
                print(f"Descripción: {config.get("description", "")}")
        result = simulator.simulate(cadena, output_file=output_file)
        print(f"Result for {config_file}: {result}")
