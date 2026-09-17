# Sesión 2 — Motor de Inferencia y Modus Ponens (Forward Chaining)

## Taller Analítico 2: Traza de Inferencia (20 min)

**Base de conocimientos:**

- R1: SI [Tiene Motor] Y [Tiene Dos Ruedas] ENTONCES [Es Motocicleta]
- R2: SI [Es Motocicleta] ENTONCES [Requiere Casco]
- R3: SI [Requiere Casco] Y [Es Menor de Edad] ENTONCES [Permiso Denegado]

**Hechos iniciales:** `{Tiene Motor: True, Tiene Dos Ruedas: True, Es Menor de Edad: True}`

### Traza del motor (Encadenamiento Hacia Adelante)

- **Ciclo 1:** se comparan las 3 reglas contra la memoria. Solo **R1** cumple (Tiene Motor=True y Tiene Dos Ruedas=True). Se dispara R1 → **nuevo hecho:** `Es Motocicleta = True`. R2 y R3 no se disparan todavía porque sus premisas (`Es Motocicleta`, `Requiere Casco`) aún no existían en memoria al inicio de este ciclo.
- **Ciclo 2:** ahora `Es Motocicleta = True` está en memoria → se cumple **R2** → se dispara → **nuevo hecho:** `Requiere Casco = True`.
- **Ciclo 3:** ahora `Requiere Casco = True` y `Es Menor de Edad = True` → se cumple **R3** → se dispara → **nuevo hecho:** `Permiso Denegado = True`.
- **Ciclo 4:** se vuelven a revisar las 3 reglas; todas sus conclusiones ya están en memoria, no hay hechos nuevos → `nuevos_hechos = False` → **el motor se detiene**.

**Memoria final:**
`{Tiene Motor: True, Tiene Dos Ruedas: True, Es Menor de Edad: True, Es Motocicleta: True, Requiere Casco: True, Permiso Denegado: True}`

---

## Taller de Laboratorio: Motor de Fraude Bancario (40 min)

**Misión práctica:**

1. Analizar el motor de inferencia dado en la sesión (el `all()` actúa como compuerta lógica AND sobre las condiciones de cada regla).
2. Transcribir el motor genérico de Forward Chaining.
3. Modificar hechos + reglas para simular un **Sistema de Detección de Fraude** (al menos 4 reglas).
4. Flujo esperado: `SI monto > 5000 → Transaccion Inusual`. `SI Transaccion Inusual Y Pais Extranjero → Bloquear Tarjeta`.
5. Ejecutar y verificar que el motor deduce el bloqueo de la tarjeta mediante el encadenamiento correcto.

Ver [`taller_laboratorio.py`](taller_laboratorio.py).
