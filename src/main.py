from validateRegex import validar_regex
from regexToSY import infix_a_postfix
from syToSyntaxTree import postfix_a_arbol_sintactico, visualizar_arbol_sintactico
from astToDFA import direct_dfa_from_ast 

def main():
    regex_entrada = input("Ingrese la expresión regular: ")

    # Validación
    if not validar_regex(regex_entrada):
        print("La expresión regular no es válida.")
        return

    # Verificar si el símbolo '$' está presente en la expresión
    if '$' in regex_entrada:
        print("Error: El símbolo '$' está reservado para indicar el final de la cadena.")
        return
    
    # Agregar el símbolo de fin de cadena '$' al final de la expresión
    if not regex_entrada.endswith('$'):
        regex_entrada += '$'

    # Conversión de infix a postfix (el proceso tokeniza, inserta concatenaciones y aplica Shunting Yard)
    try:
        postfix_tokens = infix_a_postfix(regex_entrada)

    except ValueError as error:
        print("Error al convertir a notación postfix:", error)
        return

    # Construcción del árbol sintáctico a partir de los tokens en postfix
    try:
        arbol_sintactico = postfix_a_arbol_sintactico(postfix_tokens)
        print("Árbol sintáctico construido:")
        print(arbol_sintactico)
    except ValueError as error:
        print("Error al construir el árbol sintáctico:", error)
        return

    # Visualización del árbol con Graphviz (se genera un archivo 'syntax_tree.png')
    try:
        visualizar_arbol_sintactico(arbol_sintactico, "syntax_tree")
        print("Se ha generado y abierto el archivo 'syntax_tree.png' con la visualización del árbol sintáctico.")
    except Exception as e:
        print("Error al generar la visualización con Graphviz:", e)

    # Construcción del DFA directo (no minimizado) a partir del AST usando el método followpos
    try:
        dfa_states, transitions, accepting_states, pos_dict, followpos = direct_dfa_from_ast(arbol_sintactico)
        print("\n--- DFA DIRECTO (NO MINIMIZADO) ---")
        
        # Mostrar los estados del DFA
        print("Estados DFA:")
        for state, state_id in dfa_states.items():
            # Se muestra el conjunto de posiciones (ordenado para facilitar la lectura)
            print(f"  Estado {state_id}: {sorted(list(state))}")
        
        # Mostrar las transiciones
        print("\nTransiciones:")
        for state, trans in transitions.items():
            state_id = dfa_states[state]
            for symbol, next_state in trans.items():
                next_id = dfa_states[next_state]
                print(f"  Estado {state_id} -- {symbol} --> Estado {next_id}")
        
        # Mostrar los estados de aceptación
        print("\nEstados de aceptación:")
        print(accepting_states)
    except Exception as e:
        print("Error al construir el DFA:", e)

if __name__ == "__main__":
    main()
