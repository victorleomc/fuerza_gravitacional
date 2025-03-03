import numpy as np

# Función para calcular la fuerza gravitacional entre dos cuerpos
def calcular_fuerza_gravitacional(m1, m2, r):
    G = 6.67430e-11  # Constante gravitacional en m^3 kg^-1 s^-2
    fuerza = G * (m1 * m2) / r**2
    return fuerza

if __name__ == "__main__":
    m1 = float(input("Ingrese la masa del primer cuerpo (kg): "))
    m2 = float(input("Ingrese la masa del segundo cuerpo (kg): "))
    r = float(input("Ingrese la distancia entre los dos cuerpos (m): "))
    
    # Calcular la fuerza gravitacional
    fuerza = calcular_fuerza_gravitacional(m1, m2, r)
    
    print(f"La fuerza gravitacional entre los dos cuerpos es: {fuerza:.2e} N")
