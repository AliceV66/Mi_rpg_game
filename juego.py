# Importamos los módulos específicos que necesitamos de nuestro paquete Rpg_utils.
from Rpg_utils import combate, interfaz, logica

# --- Definición de Personajes ---
jugador = {
    "nombre": "Lyra", "vida": 120, "vida_maxima": 120, "ataque": 18,
    "defensa": 10, "velocidad": 15, "prob_critico": 15 
}
enemigo = {
    "nombre": "Orco Feroz", "vida": 150, "vida_maxima": 150, "ataque": 14,
    "defensa": 12, "velocidad": 8, "prob_critico": 8
}

def iniciar_combate():
    """Función principal que maneja el bucle de combate."""
    
    interfaz.texto_lento(f"¡Un {enemigo['nombre']} salvaje aparece!")
    interfaz.esperar_jugador()

    combatientes = [jugador, enemigo]
    orden_de_turno = logica.determinar_orden_turno(combatientes)

    interfaz.texto_lento("El orden de ataque es:")
    for c in orden_de_turno:
        print(f"- {c['nombre']}")
    interfaz.esperar_jugador()

    turno = 1
    while jugador['vida'] > 0 and enemigo['vida'] > 0:
        print(f"\n--- Turno {turno} ---")
        
        for atacante in orden_de_turno:
            if atacante['vida'] <= 0: continue

            defensor = enemigo if atacante is jugador else jugador
            
            interfaz.texto_lento(f"Es el turno de {atacante['nombre']}.")
            
            daño = combate.calcular_daño(atacante, defensor)
            if combate.es_golpe_critico(atacante['prob_critico']):
                daño = int(daño * 1.5) # Los críticos hacen 50% más de daño
            
            defensor['vida'] -= daño
            interfaz.texto_lento(f"¡{atacante['nombre']} ataca y causa {daño} de daño a {defensor['nombre']}!")
            
            interfaz.mostrar_barra_de_vida(jugador['nombre'], jugador['vida'], jugador['vida_maxima'])
            interfaz.mostrar_barra_de_vida(enemigo['nombre'], enemigo['vida'], enemigo['vida_maxima'])
            interfaz.esperar_jugador()

            if defensor['vida'] <= 0: break
        
        turno += 1

    print("\n--- ¡Combate Terminado! ---")
    if jugador['vida'] > 0:
        interfaz.texto_lento("¡Has ganado la batalla!")
    else:
        interfaz.texto_lento("Has sido derrotado...")

# Este bloque asegura que el juego solo se inicie si ejecutamos este archivo directamente.
if __name__ == "__main__":
    iniciar_combate()
