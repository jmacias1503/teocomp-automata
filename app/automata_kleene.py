import json
from graphviz import Digraph

def kleene_star_automaton(json_automata):
    # Extraer componentes del autómata original
    alphabet = json_automata["alphabet"]
    states = json_automata["states"] + ["s0"]  # Agregar nuevo estado inicial
    initial_state = "s0"
    original_initial = json_automata["initial_state"]
    original_final = json_automata["final_states"]
    
    # Determinar estados finales
    # Si el estado inicial original es final, mantener los estados finales originales
    if original_initial in original_final:
        final_states = ["s0"] + original_final
    else:
        final_states = ["s0"]
    
    # Construir las transiciones
    transitions = {}
    for state in states:
        transitions[state] = {}
        if state == "s0" or state in original_final:
            # Para s0 y estados finales, transiciones como las del estado inicial original
            for symbol in alphabet:
                transitions[state][symbol] = json_automata["transitions"][original_initial].get(symbol, None)
        else:
            # Para estados no finales, mantener transiciones originales
            transitions[state] = json_automata["transitions"][state]
    
    return {
        "alphabet": alphabet,
        "states": states,
        "initial_state": initial_state,
        "final_states": final_states,
        "transitions": transitions
    }

def draw_automaton(automata, filename):
    dot = Digraph()
    
    # Definir nodos (estados)
    for state in automata["states"]:
        if state in automata["final_states"]:
            dot.node(state, shape='doublecircle')  # Estados finales con doble círculo
        else:
            dot.node(state)
    
    # Agregar flecha al estado inicial
    dot.node('_start', shape="none", label="")
    dot.edge('_start', automata["initial_state"])
    
    # Definir transiciones
    for from_state, transition in automata["transitions"].items():
        for symbol, to_state in transition.items():
            if to_state is not None:  # Evitar transiciones a None
                dot.edge(from_state, to_state, label=symbol)
    
    # Renderizar a PDF
    dot.render(filename, view=False, format='pdf')

def print_quintuple(automata, name):
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

# Leer los JSONs con los AFDs
with open("automata.json", encoding="utf-8") as read_file:
    json1 = json.load(read_file)

with open("automata2.json", encoding="utf-8") as read_file2:
    json2 = json.load(read_file2)

# Mostrar las quintuplas de los autómatas originales
print_quintuple(json1, "1 (Original)")
print_quintuple(json2, "2 (Original)")

# Realizar la estrella de Kleene para cada autómata
automata_kleene1 = kleene_star_automaton(json1)
automata_kleene2 = kleene_star_automaton(json2)

# Mostrar las quintuplas de los autómatas con la estrella de Kleene
print_quintuple(automata_kleene1, "1 (Kleene Star)")
print_quintuple(automata_kleene2, "2 (Kleene Star)")

# Generar los diagramas en PDF
draw_automaton(automata_kleene1, 'kleene_star_automata1')
draw_automaton(automata_kleene2, 'kleene_star_automata2')