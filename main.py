'''

Calcula 10.000 escenarios de ganancia/pérdida con volatilidad simple.

'''

# Código

# Importamos random
import random

# Definimos una caja, una volatibilidad simple y los escenarios
inicial = 1000
vol = 0.03
escenarios = 10000

# Creamos lista de resultados
resultados = []

for _ in range(escenarios):
    # Por cada escenario realizar un ejercicio de perdida y ganancia maxima
    cambio = random.uniform(-vol, vol)
    resultados.append(inicial * (1 + cambio))

print("Pérdida máxima:", min(resultados))
print("Ganancia máxima:", max(resultados))