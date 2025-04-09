import json
import automata_kleene 
import automata_difference
import automata_union
import automata_complemento
import automata_cpositiva
import automata_interseccion as intersection_automaton
import automata_concatenacion as cat_automaton

def main():
    # Leer los autómatas desde los archivos JSON
    with open("automata.json", encoding="utf-8") as f:
        json1 = json.load(f)
    with open("automata2.json", encoding="utf-8") as f:
        json2 = json.load(f)

    while True:
        print("\n=== MENÚ DE OPERACIONES CON AUTÓMATAS ===")
        print("1. Unión")
        print("2. Diferencia")
        print("3. Kleene para cada autómata")
        print("4. Complemento")
        print("5. Cerradura positiva")
        print("6. Intersección")
        print("7. Concatenación")  
        print("8. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            # Mostrar quintuplas originales
            automata_union.print_quintuple(json1, "1 (Original)")
            automata_union.print_quintuple(json2, "2 (Original)")
            # Realizar operación
            resultado = automata_union.union_automata(json1, json2)
            # Mostrar quintupla del resultado
            automata_union.print_quintuple(resultado, "Unión")
            automata_union.draw_automaton(resultado, 'union')
            print("Autómata de unión generado: union.pdf")
        
        elif opcion == "2":
            # Mostrar quintuplas originales
            automata_difference.print_quintuple(json1, "1 (Original)")
            automata_difference.print_quintuple(json2, "2 (Original)")
            # Realizar operación
            resultado = automata_difference.difference_automata(json1, json2)
            # Mostrar quintupla del resultado
            automata_difference.print_quintuple(resultado, "Diferencia (L1 - L2)")
            automata_difference.draw_automaton(resultado, 'difference')
            print("Autómata de diferencia generado: difference.pdf")
        
        elif opcion == "3":
            # Mostrar quintupla original del primer autómata
            automata_kleene.print_quintuple(json1, "1 (Original)")
            # Kleene para el primer autómata
            resultado1 = automata_kleene.kleene_star_automaton(json1)
            automata_kleene.print_quintuple(resultado1, "1 (Kleene Star)")
            automata_kleene.draw_automaton(resultado1, 'kleene1')
            
            # Mostrar quintupla original del segundo autómata
            automata_kleene.print_quintuple(json2, "2 (Original)")
            # Kleene para el segundo autómata
            resultado2 = automata_kleene.kleene_star_automaton(json2)
            automata_kleene.print_quintuple(resultado2, "2 (Kleene Star)")
            automata_kleene.draw_automaton(resultado2, 'kleene2')
            
            print("Autómatas con estrella de Kleene generados: kleene1.pdf y kleene2.pdf")
        
        elif opcion == "4":
            # Mostrar quintupla original
            automata_complemento.print_quintuple(json1, "Original")
            # Realizar operación
            resultado = automata_complemento.complement(json1)
            # Mostrar quintupla del resultado
            automata_complemento.print_quintuple(resultado, "Complemento")
            automata_complemento.draw_automaton(resultado, 'complemento')
            print("Autómata complemento generado: complemento.pdf")
        
        elif opcion == "5":
            # Mostrar quintupla original
            automata_cpositiva.print_quintuple(json1, "Original")
            # Realizar operación
            resultado = automata_cpositiva.positive_closure(json1)
            # Mostrar quintupla del resultado
            automata_cpositiva.print_quintuple(resultado, "Cerradura Positiva (A+)")
            automata_cpositiva.draw_automaton(resultado, 'cpositiva')
            print("Autómata con cerradura positiva generado: cpositiva.pdf")
        
        elif opcion == "6":
            # Mostrar quintuplas originales
            intersection_automaton.print_quintuple(json1, "1 (Original)")
            intersection_automaton.print_quintuple(json2, "2 (Original)")
            # Realizar operación
            resultado = intersection_automaton.intersect_automata(json1, json2)
            # Mostrar quintupla del resultado
            intersection_automaton.print_quintuple(resultado, "Intersección")
            intersection_automaton.draw_automaton(resultado, 'interseccion')
            print("Autómata de intersección generado: interseccion.pdf")
        
        elif opcion == "7":
            # Mostrar quintuplas originales
            cat_automaton.print_quintuple(json1, "1 (Original)")
            cat_automaton.print_quintuple(json2, "2 (Original)")
            # Realizar operación
            resultado = cat_automaton.concatenate(json1, json2)
            # Mostrar quintupla del resultado
            cat_automaton.print_quintuple(resultado, "Concatenación")
            cat_automaton.draw_automaton(resultado, 'concatenacion')
            print("Autómata de concatenación generado: concatenacion.pdf")
        
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()