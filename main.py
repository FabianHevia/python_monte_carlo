'''

Calcula 10.000 escenarios de ganancia/pérdida con volatilidad simple.

'''

# Código

import random

inicial = 1000
vol = 0.03
escenarios = 10000

resultados = []

for _ in range(escenarios):
    cambio = random.uniform(-vol, vol)
    resultados.append(inicial * (1 + cambio))

print("Pérdida máxima:", min(resultados))
print("Ganancia máxima:", max(resultados))