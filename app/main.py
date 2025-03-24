import sys
import json
from jsonschema import validate
import draw_automaton as drw

def main():
    try:
        with open("/app/automata.json", 'r') as f:
            automaton = json.load(f)
            drw.draw(automaton)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("File not valid")
if __name__ == "__main__":
    main()
