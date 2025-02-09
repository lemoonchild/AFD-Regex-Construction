"""
Módulo para simular la ejecución de un DFA.
Se espera que se le suministre:
  - transitions: un diccionario que mapea cada estado (número) a otro diccionario de transiciones,
      con el formato: { símbolo: estado_destino, ... }
  - initial_state: el estado inicial del DFA (número)
  - accepting_states: conjunto de estados (números) que son de aceptación.
  
El módulo incluye:
  - simulate_dfa: función que, dada una cadena de entrada, simula el DFA y devuelve True si es aceptada, False en caso contrario.
  - process_input: función que permite ingresar cadenas de forma interactiva y muestra el resultado de la simulación.
"""

def simulate_dfa(transitions, initial_state, accepting_states, input_string):
    """
    Simula el DFA sobre la cadena de entrada.
    
    Parámetros:
      - transitions: diccionario de transiciones. Ejemplo:
            { 0: {'a': 1, 'b': 0}, 1: {'a': 1, 'b': 2}, ... }
      - initial_state: estado inicial (número).
      - accepting_states: conjunto de estados finales (números).
      - input_string: cadena de entrada a procesar.
      
    Retorna:
      - True si, tras procesar la cadena, el estado actual es de aceptación.
      - False en caso contrario.
    """
    current_state = initial_state
    for symbol in input_string:
        # Si no existe transición para el símbolo en el estado actual, rechaza la cadena.
        if symbol not in transitions.get(current_state, {}):
            return False
        current_state = transitions[current_state][symbol]
    return current_state in accepting_states

def process_input(transitions, initial_state, accepting_states):
    """
    Permite al usuario ingresar cadenas para ser procesadas por el DFA.
    Por cada cadena ingresada se imprime si es aceptada o no.
    
    La función finaliza cuando el usuario ingresa una cadena vacía.
    """
    print("Ingrese cadenas para procesarlas (presione Enter sin escribir nada para salir):")
    while True:
        s = input("Cadena: ")
        if s == "":
            break
        if simulate_dfa(transitions, initial_state, accepting_states, s):
            print("  Cadena aceptada")
        else:
            print("  Cadena rechazada")

