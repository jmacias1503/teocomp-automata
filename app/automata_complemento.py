import json
from graphviz import Digraph

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

def draw_automaton(automata, filename):
    dot = Digraph()
    
    # Dibujar estados
    for state in automata["states"]:
        if state in automata["final_states"]:
            dot.node(str(state), shape='doublecircle')
        else:
            dot.node(str(state))
    
    # Marcar estado inicial
    dot.node('_start', shape="none", label="")
    dot.edge('_start', str(automata['initial_state']))
    
    # Dibujar transiciones
    for from_state, transitions in automata["transitions"].items():
        for symbol, to_state in transitions.items():
            dot.edge(str(from_state), str(to_state), label=symbol)
    
    dot.render(filename, view=True)

def print_quintuple(automata, name):
    """
    Muestra la quintupla formal del autómata en la consola.
    
    Args:
        automata (dict): Diccionario con la estructura del autómata.
        name (str): Nombre o identificador del autómata para mostrar.
    """
    print(f"\n===== Quintupla del Autómata {name} =====")
    print(f"Q (Estados): {automata['states']}")
    print(f"Σ (Alfabeto): {automata['alphabet']}")
    print(f"δ (Función de transición):")
    for state, transitions in automata['transitions'].items():
        for symbol, next_state in transitions.items():
            print(f"  δ({state}, {symbol}) = {next_state}")
    print(f"q₀ (Estado inicial): {automata['initial_state']}")
    print(f"F (Estados finales): {automata['final_states']}")
    print("=" * 40)

# Cargar el autómata desde archivo JSON
with open("automata.json", encoding="utf-8") as read_file:
    automata = json.load(read_file)

# Mostrar la quintupla del autómata original
print_quintuple(automata, "Original")

# Calcular el complemento
automata_complement = complement(automata)

# Mostrar la quintupla del autómata complemento
print_quintuple(automata_complement, "Complemento")

# Visualizar el resultado
draw_automaton(automata_complement, 'finite_automaton_complement.gv')
