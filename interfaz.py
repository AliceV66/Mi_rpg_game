"""Módulo con funciones para la interfaz de usuario y la experiencia del jugador."""

import sys
import time

def mostrar_barra_de_vida(nombre: str, vida_actual: int, vida_maxima: int, longitud: int = 20):
    """Muestra una barra de vida textual para un personaje."""
    vida_actual = max(0, vida_actual)
    porcentaje = vida_actual / vida_maxima
    bloques_llenos = int(porcentaje * longitud)
    barra = '█' * bloques_llenos
    espacio_vacio = '-' * (longitud - bloques_llenos)
    print(f"{nombre}: [{barra}{espacio_vacio}] {vida_actual}/{vida_maxima} HP")

def esperar_jugador():
    """Pausa el juego hasta que el jugador presione Enter."""
    input("\nPresiona Enter para continuar...")

def texto_lento(texto: str, velocidad: float = 0.04):
    """Imprime texto en la consola letra por letra."""
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print("")
