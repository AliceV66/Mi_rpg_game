"""Módulo para funciones de lógica y flujo del juego, como la gestión de turnos."""

def determinar_orden_turno(combatientes: list) -> list:
    """
    Ordena una lista de combatientes según su estadística de 'velocidad'.
    Los más rápidos van primero.
    """
    return sorted(combatientes, key=lambda x: x['velocidad'], reverse=True)
