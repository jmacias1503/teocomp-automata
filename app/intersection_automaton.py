def intersect(afd1, afd2):
    """
    Calcula la intersección de dos AFD.
    
    Args:
        afd1 (dict): Primer AFD.
        afd2 (dict): Segundo AFD.
    
    Returns:
        dict: AFD resultante de la intersección.
    """
    # Validar que los alfabetos sean iguales (opcional)
    if afd1["alphabet"] != afd2["alphabet"]:
        raise ValueError("Los alfabetos de los AFD no coinciden.")
    
    # Crear nuevos estados como pares (q1, q2)
    new_states = []
    new_transitions = {}
    new_initial = (afd1["initial_state"], afd2["initial_state"])
    new_final = []
    
    # Generar todos los posibles pares de estados
    for q1 in afd1["states"]:
        for q2 in afd2["states"]:
            new_state = f"({q1},{q2})"
            new_states.append(new_state)
            
            # Definir transiciones para el nuevo estado
            new_transitions[new_state] = {}
            for symbol in afd1["alphabet"]:
                next_q1 = afd1["transitions"][q1][symbol]
                next_q2 = afd2["transitions"][q2][symbol]
                new_transitions[new_state][symbol] = f"({next_q1},{next_q2})"
            
            # Marcar como final si ambos estados son finales
            if q1 in afd1["final_states"] and q2 in afd2["final_states"]:
                new_final.append(new_state)
    
    # Construir el AFD resultante
    afd_intersection = {
        "alphabet": afd1["alphabet"],
        "states": new_states,
        "initial_state": f"({afd1['initial_state']},{afd2['initial_state']})",
        "final_states": new_final,
        "transitions": new_transitions
    }
    return afd_intersection
