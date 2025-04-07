def complement(afd):
    """
    Calcula el complemento de un AFD.
    
    Args:
        afd (dict): Autómata en formato JSON/dict.
    
    Returns:
        dict: Nuevo AFD con estados finales invertidos.
    """
    afd_complement = {
        "alphabet": afd["alphabet"],
        "states": afd["states"],
        "initial_state": afd["initial_state"],
        "final_states": list(set(afd["states"]) - set(afd["final_states"])),
        "transitions": afd["transitions"]
    }
    return afd_complement
