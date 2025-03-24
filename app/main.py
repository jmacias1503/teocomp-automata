import sys
import json
from jsonschema import validate
import draw_automaton as drw

def main():
    try:
        with open("./automata.json", 'r') as f:
            automaton = json.load(f)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("File not valid")
    drw.draw(automaton)
if __name__ == "__main__":
    main()
