"""
Sesion 2 - Taller de Laboratorio: Motor de Fraude Bancario (40 MIN)
Forward Chaining: motor generico transcrito de la sesion y adaptado
a un sistema de deteccion de fraude con >= 4 reglas.
"""

# Paso 1: Base de Hechos (Memoria de Trabajo)
hechos = {
    "monto": 7500,
    "pais_extranjero": True,
}

# Hecho derivado inicial a partir del monto numerico (umbral del enunciado)
hechos["monto_mayor_5000"] = hechos["monto"] > 5000

# Paso 3: Base de Conocimientos con al menos 4 reglas
reglas = [
    {
        "id": "R1",
        "condiciones": {"monto_mayor_5000": True},
        "conclusion": {"transaccion_inusual": True},
    },
    {
        "id": "R2",
        "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
        "conclusion": {"bloquear_tarjeta": True},
    },
    {
        "id": "R3",
        "condiciones": {"bloquear_tarjeta": True},
        "conclusion": {"notificar_cliente": True},
    },
    {
        "id": "R4",
        "condiciones": {"transaccion_inusual": True, "pais_extranjero": False},
        "conclusion": {"revisar_manual": True},
    },
]


# Paso 2: Motor de Inferencia Forward Chaining (mismo patron de la sesion)
def motor_inferencia(hechos, reglas):
    nuevos_hechos = True
    while nuevos_hechos:
        nuevos_hechos = False
        for regla in reglas:
            # all() actua como compuerta AND: todas las condiciones deben cumplirse
            condiciones_cumplidas = all(
                hechos.get(k) == v for k, v in regla["condiciones"].items()
            )
            if condiciones_cumplidas:
                for clave, valor in regla["conclusion"].items():
                    if clave not in hechos:  # solo si es un HECHO NUEVO
                        hechos[clave] = valor
                        nuevos_hechos = True
                        print(f"Disparando {regla['id']} -> Nuevo hecho: {clave}={valor}")
    return hechos


# Paso 4 y 5: ejecucion y verificacion del encadenamiento
if __name__ == "__main__":
    memoria_final = motor_inferencia(hechos, reglas)
    print("\nMemoria final:", memoria_final)
    print("\n¿Tarjeta bloqueada?:", memoria_final.get("bloquear_tarjeta", False))
