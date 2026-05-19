import hashlib
import time

# MD5 con salt desconocido de 3 digitos (0 a 999), formato: MD5(password + salt)
hash_objetivo = "c59a6c90ca92d23d0fe0435c21a00e39"
diccionario = "rockyou.txt"

print("=" * 60)
print("PARTE 3 - Ataque MD5 con Salt desconocido (0-999)")
print("=" * 60)
print(f"Hash objetivo : {hash_objetivo}")
print(f"Salt          : desconocido, entre 0 y 999 (1000 valores posibles)")
print(f"Diccionario   : {diccionario}")
print("-" * 60)

inicio = time.time()
encontrado = False

print("[*] Cargando diccionario en memoria...")
with open(diccionario, "r", encoding="latin-1") as file:
    palabras = [linea.rstrip("\n") for linea in file]
total = len(palabras)
print(f"[*] {total:,} palabras cargadas. Iniciando ataque...\n")

# Pre-computar bytes de los salts y el hash objetivo una sola vez
salts_bytes = [str(i).encode("latin-1") for i in range(1000)]
objetivo_bytes = bytes.fromhex(hash_objetivo)

for i, password in enumerate(palabras):
    # Progreso cada 100.000 palabras
    if i % 100_000 == 0 and i > 0:
        transcurrido = time.time() - inicio
        velocidad = i / transcurrido
        restante = (total - i) / velocidad
        print(f"[~] {i*100/total:5.1f}% | {i:>10,} / {total:,} | "
              f"{transcurrido:.0f}s transcurridos | ~{restante:.0f}s restantes")

    pwd_bytes = password.encode("latin-1", errors="ignore")

    for salt_bytes in salts_bytes:
        if hashlib.md5(pwd_bytes + salt_bytes).digest() == objetivo_bytes:
            fin = time.time()
            print(f"\n[+] Contrasena encontrada: '{password}'")
            print(f"[+] Salt encontrado      : '{salt_bytes.decode()}'")
            print(f"[+] Tiempo total         : {fin - inicio:.4f} segundos")
            encontrado = True
            break

    if encontrado:
        break

fin = time.time()
if not encontrado:
    print("[-] Contrasena no encontrada.")
print(f"[+] Tiempo total: {fin - inicio:.4f} segundos")
