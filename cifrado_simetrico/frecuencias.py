from collections import Counter


mensaje = """
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXJI AXT OKXJHX DIDZTEK V TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.
"""

frecuencias_es = {
    'e': 16.78,
    'a': 11.96,
    'o': 8.69,
    'l': 8.37,
    's': 7.88,
    'n': 7.01,
    'd': 6.87,
    'r': 4.94,
    'u': 4.80,
    'i': 4.15,
    't': 3.31,
    'c': 2.92,
    'p': 2.776,
    'm': 2.12,
    'y': 1.54,
    'q': 1.53,
    'b': 0.92,
    'g': 0.73,
    'f': 0.52,
    'v': 0.39,
    'j': 0.30,
    'ñ': 0.29,
    'z': 0.15
}

letras = [
    letra.lower()
    for letra in mensaje
    if letra.isalpha()
]

frecuencias = Counter(letras)


print("FRECUENCIAS DEL MENSAJE")

for letra, cantidad in frecuencias.most_common():

    porcentaje = cantidad / len(letras) * 100

    print(
        f"{letra} -> "
        f"{cantidad} veces "
        f"({porcentaje:.2f}%)"
    )

sustituciones = {}

def descifrar():

    resultado = ""

    for caracter in mensaje:

        letra = caracter.lower()

        if letra in sustituciones:

            nueva = sustituciones[letra]

            if caracter.isupper():
                nueva = nueva.upper()

            resultado += nueva

        else:

            resultado += "_"

    return resultado

while True:

    print("\n")
    print("ATAQUE INTERACTIVO")

    print("\nSustituciones actuales:")

    if sustituciones:
        for cifrada, original in sustituciones.items():
            print(f"  {cifrada} -> {original}")
    else:
        print("  Ninguna")

    print("\nMensaje:")
    print(descifrar())

    print("\nOpciones:")
    print("1. Añadir/cambiar sustitución")
    print("2. Eliminar sustitución")
    print("3. Mostrar frecuencias")
    print("4. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":

        cifrada = input(
            "Letra cifrada: "
        ).lower()

        original = input(
            "Letra que crees que representa: "
        ).lower()

        sustituciones[cifrada] = original

        print(
            f"\nAñadido: {cifrada} -> {original}"
        )

    elif opcion == "2":

        cifrada = input(
            "Letra cifrada que quieres eliminar: "
        ).lower()

        if cifrada in sustituciones:

            del sustituciones[cifrada]

            print("Sustitución eliminada")

        else:

            print("Esa letra no tiene sustitución")

    elif opcion == "3":

        print("\nFrecuencia del criptograma:")

        for letra, cantidad in frecuencias.most_common():

            porcentaje = cantidad / len(letras) * 100

            print(
                f"{letra}: "
                f"{porcentaje:.2f}%"
            )

        print("\nFrecuencia del castellano:")

        for letra, frecuencia in frecuencias_es.items():

            print(
                f"{letra}: "
                f"{frecuencia}%"
            )

    elif opcion == "4":

        print("\nFin programa")
        break

    else:

        print("\nOpción no válida")