"""Módulo con funciones relacionadas al cálculo y la aleatoriedad del combate."""

import random

def tirar_dado(caras: int) -> int:
    """Simula la tirada de un dado con un número específico de caras."""
    return random.randint(1, caras)

def calcular_daño(atacante: dict, defensor: dict) -> int:
    """Calcula el daño de un ataque, con una pequeña variación aleatoria."""
    variacion_ataque = random.randint(-2, 3)
    ataque_total = atacante['ataque'] + variacion_ataque
    daño = ataque_total - defensor['defensa']
    return max(0, daño) # El daño nunca es negativo

def es_golpe_critico(probabilidad: int) -> bool:
    """Determina si un ataque es un golpe crítico basado en una probabilidad."""
    tirada = random.randint(1, 100)
    if tirada <= probabilidad:
        print("¡GOLPE CRÍTICO!")
        return True
    return False
