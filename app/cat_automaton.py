import json

def concatenate(afd1, afd2):
    """
    Concatena dos AFD y devuelve un AFN (con ε-transiciones).
    
    Args:
        afd1 (dict): Primer AFD.
        afd2 (dict): Segundo AFD.
    
    Returns:
        dict: AFN resultante con ε-transiciones.
    """
    # Renombrar estados para evitar colisiones
    afd1_states = {f"1_{state}" for state in afd1["states"]}
    afd2_states = {f"2_{state}" for state in afd2["states"]}

    # Combinar transiciones y añadir ε-transiciones
    new_transitions = {}

    # Procesar AFD1
    for state in afd1["states"]:
        new_state = f"1_{state}"
        new_transitions[new_state] = {
            symbol: f"1_{afd1['transitions'][state][symbol]}"
            for symbol in afd1["alphabet"]
        }
        if state in afd1["final_states"]:
            new_transitions[new_state]["ε"] = f"2_{afd2['initial_state']}"

    # Procesar AFD2
    for state in afd2["states"]:
        new_state = f"2_{state}"
        new_transitions[new_state] = {
            symbol: f"2_{afd2['transitions'][state][symbol]}"
            for symbol in afd2["alphabet"]
        }

    # Crear AFN resultante
    afn_result = {
        "alphabet": sorted(list(set(afd1["alphabet"] + afd2["alphabet"]))),
        "states": sorted(list(afd1_states.union(afd2_states))),
        "initial_state": f"1_{afd1['initial_state']}",
        "final_states": [f"2_{state}" for state in afd2["final_states"]],
        "transitions": new_transitions
    }
    return afn_result

def load_automata_from_json(file_path):
    """Carga los AFD desde un archivo JSON."""
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data["automaton1"], data["automaton2"]
