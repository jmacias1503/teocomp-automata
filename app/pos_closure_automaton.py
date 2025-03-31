def positive_closure(afd):
    """
    Calcula la cerradura positiva (A+) de un AFD.
    
    Args:
        afd (dict): Autómata en formato JSON/dict.
    
    Returns:
        dict: AFN resultante con ε-transiciones.
    """
    # Copiar el AFD original para no modificarlo directamente
    afn_result = {
        "alphabet": afd["alphabet"],
        "states": afd["states"],
        "initial_state": afd["initial_state"],
        "final_states": afd["final_states"],
        "transitions": {state: {**trans} for state, trans in afd["transitions"].items()}
    }
    
    # Añadir ε-transiciones desde cada estado final al estado inicial
    for final_state in afd["final_states"]:
        if "ε" not in afn_result["transitions"][final_state]:
            afn_result["transitions"][final_state]["ε"] = afd["initial_state"]
        else:
            # Si ya existe una ε-transición, añadir el destino como lista
            if isinstance(afn_result["transitions"][final_state]["ε"], str):
                afn_result["transitions"][final_state]["ε"] = [afn_result["transitions"][final_state]["ε"], afd["initial_state"]]
            else:
                afn_result["transitions"][final_state]["ε"].append(afd["initial_state"])
    
    return afn_result
