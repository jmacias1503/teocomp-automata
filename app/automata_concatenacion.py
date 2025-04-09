import json
from graphviz import Digraph

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
            if isinstance(to_state, list):
                # Si hay múltiples destinos para un símbolo
                for dest in to_state:
                    dot.edge(str(from_state), str(dest), label=symbol)
            else:
                # Si hay un solo destino
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
    
    # Determinar si hay ε-transiciones para incluirla en el alfabeto
    has_epsilon = False
    for _, transitions in automata['transitions'].items():
        if 'ε' in transitions:
            has_epsilon = True
            break
            
    alphabet_display = automata['alphabet']
    if has_epsilon:
        alphabet_display = alphabet_display + ['ε']
        
    print(f"Σ (Alfabeto): {alphabet_display}")
    print(f"δ (Función de transición):")
    for state, transitions in automata['transitions'].items():
        for symbol, next_state in transitions.items():
            print(f"  δ({state}, {symbol}) = {next_state}")
    print(f"q₀ (Estado inicial): {automata['initial_state']}")
    print(f"F (Estados finales): {automata['final_states']}")
    print("=" * 40)

# Cargar los autómatas desde archivos JSON
with open("automata.json", encoding="utf-8") as read_file:
    json1 = json.load(read_file)

with open("automata2.json", encoding="utf-8") as read_file2:
    json2 = json.load(read_file2)

# Mostrar las quintuplas de los autómatas originales
print_quintuple(json1, "1 (Original)")
print_quintuple(json2, "2 (Original)")

# Realizar la concatenación
automata_concatenation = concatenate(json1, json2)

# Mostrar la quintupla del autómata resultante
print_quintuple(automata_concatenation, "Concatenación")

# Visualizar el resultado
draw_automaton(automata_concatenation, 'finite_automaton_concatenation.gv')
