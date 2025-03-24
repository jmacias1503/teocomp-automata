import sys
import json
from jsonschema import validate
import draw_automaton as drw

def main():
    if len(sys.argv) != 2:
        print("Use: python3 main.py <json file>")
        sys.exit(1)
    json_file = sys.argv[1]
    try:
        with open(json_file, 'r') as f:
            automaton = json.load(f)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("File not valid")
    drw.draw(automaton)
if __name__ == "__main__":
    main()
