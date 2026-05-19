# Ataque de Fuerza Bruta con Diccionario

**Privacidad y Seguridad | Trabajo Práctico**

---

## Parte 1 — Ataque de diccionario con SHA-256

### 1.1 Identificación del algoritmo

El hash tiene 64 caracteres hexadecimales, lo que equivale a 256 bits. Eso lo identifica como SHA-256. MD5 produce 32 hex (128 bits) y SHA-1 produce 40 hex (160 bits).

| Campo               | Valor                                                              |
|---------------------|--------------------------------------------------------------------|
| Hash objetivo       | `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` |
| Algoritmo           | SHA-256 (64 hex = 256 bits)                                        |
| Contraseña encontrada | `password`                                                       |
| Tiempo de ejecución | 0.0013 segundos                                                    |

### 1.2 Análisis del resultado

La contraseña `password` aparece al inicio del diccionario `rockyou.txt`, por eso el ataque termina en menos de 2 milisegundos. El tiempo depende de cuán temprano aparezca la palabra en el diccionario, no del algoritmo.

---

## Parte 2 — MD5 con salt conocido

### 2.1 Resultado del ataque

| Campo               | Valor                              |
|---------------------|------------------------------------|
| Hash objetivo       | `2484b2d1aec71de2ca87f88af401a6af` |
| Salt                | `99`                               |
| Formato             | MD5(password + salt)               |
| Contraseña encontrada | `password`                       |
| Tiempo de ejecución | 0.0013 segundos                    |

### 2.2 ¿Tardó más o menos que la Parte 1?

Tardó lo mismo: **0.0013 segundos en ambos casos**. La contraseña es `password`, que aparece al inicio del diccionario. Con salt conocido, el script solo concatena el sufijo antes de hashear, lo que no cambia cuántas palabras hay que probar. El costo extra por concatenación es insignificante.

**Un salt conocido no aporta protección real.** Si el atacante tiene el hash y el salt, el ataque de diccionario funciona igual que sin salt.

---

## Parte 3 — MD5 con salt desconocido (0–999)

### 3.1 Resultado del ataque

| Campo               | Valor                              |
|---------------------|------------------------------------|
| Hash objetivo       | `c59a6c90ca92d23d0fe0435c21a00e39` |
| Contraseña encontrada | `qwerty`                         |
| Salt encontrado     | `741`                              |
| Tiempo de ejecución | 2.4826 segundos                    |

### 3.2 ¿Por qué el salt de solo 3 dígitos aumentó tanto el tiempo?

Cuando el salt es desconocido, hay que probar cada contraseña contra los 1000 posibles salts (0–999) antes de descartarla, en lugar de una sola vez.

El cálculo:

- Parte 1: 14.344.392 hashes (1 por palabra)
- Parte 3: hasta 14.344.392.000 hashes posibles (1000 × palabras)

El tiempo pasó de 0.0013s a 2.48s porque `qwerty` aparece más adelante en el diccionario que `password`, y para cada palabra se recorre el espacio completo de salts. El resultado es un aumento de hasta **1000×** en el trabajo total.

### 3.3 ¿Sería posible este ataque con un salt de 16 caracteres aleatorios?

No. Un salt de 16 caracteres del juego ASCII imprimible (~95 símbolos) tiene un espacio de:

```
95^16 ≈ 4.4 × 10^31 combinaciones posibles
```

Una GPU moderna calcula unos 10 mil millones de hashes MD5 por segundo. Aun así, recorrer ese espacio tomaría del orden de **10^14 años**. El ataque no es viable.

Esto es lo que hacen sistemas modernos como bcrypt o Argon2: salts aleatorios de 16–32 bytes almacenados junto al hash. El salt no tiene que ser secreto; su función es que dos usuarios con el mismo password tengan hashes distintos, obligando al atacante a repetir el trabajo individualmente para cada cuenta.

### 3.4 ¿Qué es más seguro: SHA-256 sin salt o MD5 con salt desconocido?

En la práctica, **MD5 con un salt secreto y suficientemente largo es más resistente** que SHA-256 sin salt, para un atacante que ya tiene la base de datos de hashes.

**SHA-256 sin salt:**

- Permite rainbow tables: tablas precalculadas que mapean hashes a contraseñas.
- Si dos usuarios tienen el mismo password, sus hashes son idénticos.
- El hash de la Parte 1 aparece inmediatamente en cualquier lookup online.

**MD5 con salt desconocido largo:**

- Las rainbow tables son inútiles: el mismo password produce un hash diferente cada vez.
- El atacante tiene que calcular desde cero para cada cuenta, sin reutilizar trabajo.

Dicho esto, ambas opciones son malas. SHA-256 es demasiado rápido para almacenar contraseñas, y MD5 tiene vulnerabilidades de colisión conocidas. Lo correcto es usar **bcrypt**, **Argon2id** o **scrypt**, que tienen un costo computacional configurable y hacen que cada intento de fuerza bruta sea mucho más caro.
