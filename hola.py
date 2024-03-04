# prueba

print("Hola mundo")

import numpy as np

# Definir la función q-Gaussiana
def q_gaussian(x, A, q, beta):
    return A * ((1 + beta * (q - 1) * (x**2))**(1 / (1 - q)))

# Generar datos de ejemplo
x_data = np.linspace(-1000, 1000, 1001)
y_data = q_gaussian(x_data, A=1, q=2.38, beta=1) + np.random.normal(0, 0.0001, size=len(x_data))

print(np.max(y_data))
print(q_gaussian(0, A=1, q=2.38, beta=1)) 

# Graficar los datos y el ajuste
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data/np.max(y_data), label='Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.yscale('log')
plt.legend()
plt.show()

