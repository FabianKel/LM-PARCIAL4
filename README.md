# LM-PARCIAL4
El Parcial consiste en elaborar un programa que simule una máquina de Turing determinista, tomando en cuenta que debe utilizarse la notación vista en clase. 

## Contenido

* Configuración de la máquina de turing y sus componentes en [config.yaml](./config.yaml)
* Script para cargar la configuración leyendo el archivo [config_loader.py](./config_loader.py)
* Script para crear la máquina de turing [turing_machine.py](./turing_machine.py)
* Script para simular la máquina de turing [simulator.py](./simulator.py)
* Ejecución del programa y definición de la cadena de entrada [main.py](./main.py)

* Para los ejemplos para Aceptación, Rechazo y Bucle, se utilizarán las siguientes cadenas de entrada:
- Aceptación: `001` en [configAccept.yml](./configAccept.yaml)
- Rechazo: `1111` en [configReject.yml](./configReject.yaml)
- Bucle: `01111111` en [configLoop.yml](./configLoop.yaml)

## Dependencias
Yaml
``` bash
pip install pyyaml
```

## Configuración de la Máquina en [config.yaml](./config.yaml):

La máquina consite en una 7 tupla, (Q,Σ,Γ,δ,q0,qaccept,q reject):

* Q: Conjunto de estados.
* Σ: Alfabeto de entrada.
* Γ: Alfabeto de la cinta (incluye símbolos de blanco ⊔).
* δ: Función de transición.
* q0: Estado inicial.
* q_accept: Estado de aceptación.
* q_reject: Estado de rechazo.
* cadena: Cadena utilizada para la simulación, en caso de estar vacía se le solicita al usuario

