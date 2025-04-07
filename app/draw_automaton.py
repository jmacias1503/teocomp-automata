import json
from graphviz import Digraph

def draw(automaton_data):
  alphabet = automaton_data.get("alphabet", [])
  states = automaton_data.get("states", [])
  initial_state = automaton_data.get("initial_state", "")
  final_states = automaton_data.get("final_states", [])
  transitions = automaton_data.get("transitions", {})
  
  # Draw the automata
  dot = Digraph()
  
  for state in states:
      if state in final_states:
          dot.node(state, shape='doublecircle')  
      else:
          dot.node(state)  
  
  dot.node('_start', shape="none", label="")
  dot.edge('_start', initial_state)
  
  for from_state, transition in transitions.items():
      for symbol, to_state in transition.items():
          dot.edge(from_state, to_state, label=symbol)
  
  dot.render('finite_automaton.gv', view=True)
