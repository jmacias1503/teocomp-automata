# Automata teoria de la computacion

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
