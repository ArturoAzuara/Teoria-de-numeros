print("""
       **************************************
       *       'CIFRADO DE MENSAJES'        * 
       *         'FES Aragón UNAM'          *
       *      'Ingeniería en Computación'   *
       *     Azuara Ocotitla Arturo Ivan    *
       *    Monroy Quintero Eliezer Isaí    *
       *   Padron Cortes Monica Alessandra  *
       *       Villela Andrade Aksel        *
       **************************************
    """)


def comp_1er_num_primo(numero_p):
    numero_primo = True
    if numero_p <= 1:
        numero_primo = False
    else:
        for i in range(2, numero_p):
            if numero_p % i == 0:
                numero_primo = False
                break
    if not numero_primo:
        print("El 1er número no es primo, intentalo de nuevo.")
    return numero_primo


def comp_2nd_num_primo(numero_q):
    numero_primo = True
    if numero_q <= 1:
        numero_primo = False
    else:
        for i in range(2, numero_q):
            if numero_q % i == 0:
                numero_primo = False
                break
    if not numero_primo:
        print("El 2nd número no es primo, intentalo de nuevo.")
    return numero_primo


def num_iguales(numero_p, numero_q):
    if numero_q == numero_p:
        print("Los numeros no pueden ser los mismos, intenta nuevamente.")
        return True
    else:
        return False


try:
    numero_p = int(input("Introduce 1er numero primo: "))
    while not comp_1er_num_primo(numero_p):
        numero_p = int(input("Introduce 1er numero primo: "))

    numero_q = int(input("Introduce 2nd numero primo: "))
    while not comp_2nd_num_primo(numero_q) or num_iguales(numero_p, numero_q):
        numero_q = int(input("Introduce 2nd numero primo: "))
    print(f"Los numeros introducidos han sido, {numero_p} y {numero_q}.")

    producto_n = numero_p * numero_q
    print(f"El resultado del producto de 'n' es: {producto_n}")
    producto_de_phi = (numero_p - 1) * (numero_q - 1)
    print(f"El resultado del producto de 'z' es: {producto_de_phi}")
    mcd = int(input("Introduce un numero coprimo con phi: "))


except ValueError:
    print("Error, intenta de nuevo")
