import hashlib
import time

# MD5 con salt conocido, formato: MD5(password + salt)
hash_objetivo = "2484b2d1aec71de2ca87f88af401a6af"
salt = "99"
diccionario = "rockyou.txt"

print("=" * 55)
print("PARTE 2 - Ataque de diccionario MD5 con Salt conocido")
print("=" * 55)
print(f"Hash objetivo : {hash_objetivo}")
print(f"Salt          : '{salt}'")
print(f"Formato       : MD5(password + salt)")
print(f"Diccionario   : {diccionario}")
print("-" * 55)

inicio = time.time()
encontrado = False

with open(diccionario, "r", encoding="latin-1") as file:
    for linea in file:
        password = linea.rstrip("\n")
        if hashlib.md5((password + salt).encode("latin-1")).hexdigest() == hash_objetivo:
            print(f"\n[+] Contrasena encontrada: '{password}'")
            encontrado = True
            break

fin = time.time()
if not encontrado:
    print("\n[-] Contrasena no encontrada en el diccionario.")
print(f"[+] Tiempo total: {fin - inicio:.4f} segundos")
