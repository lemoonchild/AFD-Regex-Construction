def validar_regex(regex: str) -> bool:
    """
    Valida que la expresión regular sólo contenga los caracteres permitidos:
    - Operandos: letras (a-z, A-Z), dígitos (0-9) y el símbolo '#' para cadena vacía.
    - Operadores: '+', '.', '*' y paréntesis '(' y ')'.
    
    También verifica que los paréntesis estén balanceados.
    """
    caracteres_validos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#()+.*")
    for ch in regex:
        if ch not in caracteres_validos:
            print(f"Caracter inválido encontrado: '{ch}'")
            return False

    # Verificar que los paréntesis estén balanceados
    pila = []
    for ch in regex:
        if ch == '(':
            pila.append(ch)
        elif ch == ')':
            if not pila:
                print("Error: Paréntesis de cierre sin correspondencia.")
                return False
            pila.pop()
    if pila:
        print("Error: Paréntesis de apertura sin correspondencia.")
        return False
    return True
