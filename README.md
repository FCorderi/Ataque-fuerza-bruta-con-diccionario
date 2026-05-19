# Ataque de fuerza bruta con diccionario

Ejercicio para Privacidad y Seguridad sobre ataque de fuerza bruta con diccionario a una contraseña hasheada.

---

## Primera Parte

Has obtenido el hash de un usuario de un sitio que no usa protección adicional.

**Hash:** `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8`

1. Identifica el algoritmo utilizado para realizar el hash.
2. Utilizando el diccionario `rockyou.txt` intenta encontrar la contraseña del usuario.

> **NOTA:** Medir cuánto tiempo tarda el script (pueden usar la librería `time` de Python, o análoga según el lenguaje que deseen utilizar).

---

## Segunda Parte

Resulta que ahora obtienes de otro sitio el hash de una contraseña. Sabes de antemano que este sitio utiliza el algoritmo MD5 y un Salt para "compensar" las debilidades conocidas de MD5.

**Hash:** `2484b2d1aec71de2ca87f88af401a6af`  
**Salt:** `99`

Se pide que se modifique y entregue un nuevo código capaz de encontrar la contraseña del usuario del sitio 2.

¿Esta segunda parte tardó más o menos que la Parte 1?

---

## Tercera Parte

El sistema es igual al anterior pero no conoces el Salt. Solo sabes que es un número de 3 dígitos.

**Hash:** `c59a6c90ca92d23d0fe0435c21a00e39`

Intenta averiguar la contraseña.

**Conteste:**

1. ¿Por qué el Salt de solo 3 dígitos aumentó tanto el tiempo?
2. Si el Salt fuera de 16 caracteres aleatorios (como en sistemas modernos), ¿sería posible este ataque?
3. ¿Qué es más seguro: un algoritmo fuerte (SHA-256) sin salt, o uno débil (MD5) con un salt que el atacante no conoce?

---

## Tip para el código (recomendado Python)

```python
import time

inicio = time.time()
# ... acá va el bucle de fuerza bruta ...

# Abrir el archivo con encoding 'latin-1' para evitar errores de lectura
with open(diccionario, 'r', encoding='latin-1') as file:
    for linea in file:
        # Conviene borrar el salto de línea al final de cada palabra
        # para que no sea incluido como parte del string

fin = time.time()

print(f"Tiempo total: {fin - inicio} segundos")
```
