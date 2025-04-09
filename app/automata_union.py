import json
from graphviz import Digraph
from itertools import product #Necesario para el producto cartesiano de estados

def union_automata(json1, json2):
    alphabet = list(set(json1["alphabet"]) | set(json2["alphabet"])) #set elimina duplicados
    states = list(product(json1["states"], json2["states"])) 
    initial_state = (json1["initial_state"], json2["initial_state"])
    final_states = [
    state for state in states
    if state[0] in json1["final_states"] or state[1] in json2["final_states"]
    ]

    transitions = {} #Crear un diccionario para las transiciones vacio
    for state in states: #Se recorre sobre cada estado combinado
        state1, state2 = state
        transitions[state] = {}
        for symbol in alphabet:
            next_state1 = json1["transitions"].get(state1, {}).get(symbol, state1)
            next_state2 = json2["transitions"].get(state2, {}).get(symbol, state2)
            transitions[state][symbol] = (next_state1, next_state2)
    
    return {
        "alphabet": alphabet,
        "states": states,
        "initial_state": initial_state,
        "final_states": final_states,
        "transitions": transitions
    }

def draw_automaton(automata, filename):
    dot = Digraph()
    
    for state in automata["states"]:
        label = f"({state[0]},{state[1]})"
        if state in automata["final_states"]:
            dot.node(label, shape='doublecircle')
        else:
            dot.node(label)
    
    initial_label = f"({automata['initial_state'][0]},{automata['initial_state'][1]})"
    dot.node('_start', shape="none", label="")
    dot.edge('_start', initial_label)
    
    for from_state, transition in automata["transitions"].items():
        from_label = f"({from_state[0]},{from_state[1]})"
        for symbol, to_state in transition.items():
            to_label = f"({to_state[0]},{to_state[1]})"
            dot.edge(from_label, to_label, label=symbol)
    
    dot.render(filename, view=True)

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

with open("automata.json", encoding="utf-8") as read_file:
    json1 = json.load(read_file)

with open("automata2.json", encoding="utf-8") as read_file2:
    json2 = json.load(read_file2)

# Mostrar quintuplas de los autómatas originales
print_quintuple(json1, "1")
print_quintuple(json2, "2")

# Generar autómata unión y mostrar su quintupla
automata_union = union_automata(json1, json2)
print_quintuple(automata_union, "Unión")

draw_automaton(automata_union, 'finite_automaton_union.gv')