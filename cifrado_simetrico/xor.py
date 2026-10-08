def xor_bytes(mensaje, clave):
    resultado = bytearray()

    for i in range(len(mensaje)):
        resultado.append(mensaje[i] ^ clave[i])

    return bytes(resultado)


# Leer datos
mensaje = input("Mensaje: ")
clave = input("Clave: ")

# Convertir a bytes ASCII
mensaje_bytes = mensaje.encode("ascii")
clave_bytes = clave.encode("ascii")

# Comprobar que tienen la misma longitud
if len(mensaje_bytes) != len(clave_bytes):
    print("\nError: el mensaje y la clave deben tener la misma longitud.")
    print(f"Longitud del mensaje: {len(mensaje_bytes)} bytes")
    print(f"Longitud de la clave:   {len(clave_bytes)} bytes")
    exit()


# Cifrado XOR
criptograma = xor_bytes(mensaje_bytes, clave_bytes)

# Descifrado XOR
mensaje_descifrado = xor_bytes(criptograma, clave_bytes)


# Mostrar resultados en hexadecimal
print("\n--- RESULTADOS ---")

print("Mensaje:     ", mensaje_bytes.hex())
print("Clave:       ", clave_bytes.hex())
print("Criptograma: ", criptograma.hex())

# Comprobación
print("\n--- COMPROBACIÓN ---")

print("Mensaje descifrado:", mensaje_descifrado.decode("ascii"))

if mensaje_descifrado == mensaje_bytes:
    print("El descifrado coincide exactamente con el mensaje original.")
else:
    print("El descifrado NO coincide con el mensaje original.")