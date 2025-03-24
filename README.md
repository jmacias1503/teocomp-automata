# Automata teoria de la computacion

## Leer y guardar datos
- Cada operacion se manejara por un modulo (archivo)
- El programa se ejecutará cpasando como argumento un archivo JSON, con la siguiente estructura:
```json
{
    "alphabet": ["a", "b"],
    "states": ["1", "2"],
    "initial_state": "1",
    "final_states": "2",
    "transitions": {
        "1": {
            "a": "1",
            "b": "2"
        },
        "2": {
            "a": "2",
            "b": "1"
        }
    }
}
```
- Mediante el uso de la librearia "json" se leeran los archivos JSON y se guardaran los datos dentro de el script de Python

## Operaciones entre Autómatas Finitos Deterministas (AFD)

- Una vez leído y guardado el o los archivos JSON , el script debe de ser capaz de concretar las siguientes operaciones:
- Complemento
- Unión
- Intersección
- Resta
- Concatenación
- Estrella de Kleene
- Cerradura positiva.

## Outpot del script

- El script tiene que mostrar en salida los siguientes requerimientos:
- La quíntupla de el/los AFD (dependiendo el caso)
- Diagrama de el/los AFD
- La quíntupla del resultado de la operación
- Modelo de transición
- Diagrama del AFD resultante de la operación.
