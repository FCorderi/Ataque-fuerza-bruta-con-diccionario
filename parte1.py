import hashlib
import time

# SHA-256: 64 caracteres hexadecimales = 256 bits
hash_objetivo = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
diccionario = "rockyou.txt"

print("=" * 55)
print("PARTE 1 - Ataque de diccionario con SHA-256")
print("=" * 55)
print(f"Hash objetivo : {hash_objetivo}")
print(f"Algoritmo     : SHA-256 ({len(hash_objetivo)} hex = {len(hash_objetivo)*4} bits)")
print(f"Diccionario   : {diccionario}")
print("-" * 55)

inicio = time.time()
encontrado = False

with open(diccionario, "r", encoding="latin-1") as file:
    for linea in file:
        password = linea.rstrip("\n")
        if hashlib.sha256(password.encode("latin-1")).hexdigest() == hash_objetivo:
            print(f"\n[+] Contrasena encontrada: '{password}'")
            encontrado = True
            break

fin = time.time()
if not encontrado:
    print("\n[-] Contrasena no encontrada en el diccionario.")
print(f"[+] Tiempo total: {fin - inicio:.4f} segundos")
