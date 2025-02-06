from validateRegex import validar_regex
from regexToSY import insertar_operador_concatenacion, infix_a_postfix
from syToSyntaxTree import postfix_a_arbol_sintactico

def main():
    # Solicitar al usuario la expresión regular
    regex_entrada = input("Ingrese la expresión regular: ")

    # Validar la expresión regular
    if not validar_regex(regex_entrada):
        print("La expresión regular no es válida.")
        return

    # Inserción de operadores de concatenación (para convertir concatenaciones implícitas en explícitas)
    regex_concatenada = insertar_operador_concatenacion(regex_entrada)
    print("Expresión regular con concatenación explícita:", regex_concatenada)

    # Conversión de infix a postfix
    try:
        postfix = infix_a_postfix(regex_concatenada)
        print("Expresión en notación postfix:", postfix)
    except ValueError as error:
        print("Error al convertir a notación postfix:", error)
        return

    # Construcción del árbol sintáctico a partir de la expresión en postfix
    try:
        arbol_sintactico = postfix_a_arbol_sintactico(postfix)
        print("Árbol sintáctico construido:")
        print(arbol_sintactico)
    except ValueError as error:
        print("Error al construir el árbol sintáctico:", error)
        return

if __name__ == "__main__":
    main()
