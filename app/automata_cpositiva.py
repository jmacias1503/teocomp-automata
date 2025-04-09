import json
from graphviz import Digraph

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

def draw_automaton(automata, filename):
    """
    Genera una visualización gráfica del autómata.
    
    Args:
        automata (dict): Autómata a visualizar
        filename (str): Nombre del archivo de salida
    """
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
        for symbol, to_states in transitions.items():
            if isinstance(to_states, list):
                # Si hay múltiples destinos para un símbolo (caso de AFN)
                for to_state in to_states:
                    dot.edge(str(from_state), str(to_state), label=symbol)
            else:
                # Si hay un solo destino (caso común)
                dot.edge(str(from_state), str(to_states), label=symbol)
    
    # Renderizar y mostrar el grafo
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
    print(f"Σ (Alfabeto): {automata['alphabet'] + ['ε'] if 'ε' in str(automata['transitions']) else automata['alphabet']}")
    print(f"δ (Función de transición):")
    for state, transitions in automata['transitions'].items():
        for symbol, next_state in transitions.items():
            print(f"  δ({state}, {symbol}) = {next_state}")
    print(f"q₀ (Estado inicial): {automata['initial_state']}")
    print(f"F (Estados finales): {automata['final_states']}")
    print("=" * 40)

# Ejecutar cuando se llama directamente
if __name__ == "__main__":
    # Cargar el autómata desde archivo JSON
    with open("automata.json", encoding="utf-8") as read_file:
        automata = json.load(read_file)
    
    # Mostrar la quintupla del autómata original
    print_quintuple(automata, "Original")
    
    # Calcular la cerradura positiva
    positive_closure_automata = positive_closure(automata)
    
    # Mostrar la quintupla del autómata resultante
    print_quintuple(positive_closure_automata, "Cerradura Positiva (A+)")
    
    # Visualizar el resultado
    draw_automaton(positive_closure_automata, 'positive_closure_automaton.gv')
    
    print("Cerradura positiva calculada y visualizada con éxito.")
