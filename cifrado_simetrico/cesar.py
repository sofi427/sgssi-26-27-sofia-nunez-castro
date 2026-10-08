#!/usr/bin/env python3
from langdetect import DetectorFactory, detect


ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CRIPTOGRAMA = 'Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb'

DetectorFactory.seed = 0


def descifrar(criptograma, clave):
    """Descifra un texto César conservando mayúsculas y minúsculas."""
    salida = []
    for simbolo in criptograma:
        if simbolo.isupper():
            alfabeto = ALFABETO
        elif simbolo.islower():
            alfabeto = ALFABETO.lower()
        else:
            salida.append(simbolo)
            continue

        posicion = alfabeto.index(simbolo)
        salida.append(alfabeto[(posicion - clave) % len(alfabeto)])

    return ''.join(salida)


def recuperar_clave(criptograma):
    """Devuelve la primera candidata que langdetect identifica como español."""
    for clave in range(1, len(ALFABETO)):
        salida = descifrar(criptograma, clave)
        idioma = detect(salida)
        if idioma == 'es':
            return clave, salida

    raise ValueError('No se encontró una candidata en español')


if __name__ == '__main__':
    clave, mensaje = recuperar_clave(CRIPTOGRAMA)
    print(f'Clave recuperada: {clave}')
    print(f'Mensaje descifrado: {mensaje}')