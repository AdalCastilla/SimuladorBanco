import numpy as np
import queue
import time

# 1. Definición de lambda (tasa de llegada de clientes por hora)
lmbda = 20  # Por ejemplo, 10 clientes por hora

# 3. Implementación de la cola y las cajas de atención
cola = queue.Queue()
cajas = [None] * 4  # 4 cajas de atención

total_clientes = 0  # Para llevar la cuenta de cuántos clientes han llegado en total

# 4. Función para simular la atención de clientes
def atender_clientes(hora, momentos_llegada):
    global total_clientes

    print(f"\nHora {hora+1}:")

    for minuto in range(60):
        while momentos_llegada and momentos_llegada[0] == minuto:
            total_clientes += 1
            cola.put(total_clientes)
            print(f"Minuto {minuto}: Llegó el cliente {total_clientes}.")
            momentos_llegada.pop(0)

        # Atender clientes en cajas
        for i in range(4):
            if cajas[i]:
                cajas[i][1] -= 1
                if cajas[i][1] == 0:  # Cliente ha sido atendido
                    print(f"Minuto {minuto}: Caja {i+1}: Cliente {cajas[i][0]} atendido.")
                    cajas[i] = None
        # Mover clientes de la cola a cajas vacías
        for i in range(4):
            if cajas[i] is None and not cola.empty():
                cliente = cola.get()
                tiempo_atencion = np.random.randint(5, 16)  # Tiempo de atención entre 1 y 10 minutos
                cajas[i] = [cliente, tiempo_atencion]
                print(f"Minuto {minuto}: Caja {i+1}: Cliente {cliente} atendido durante {tiempo_atencion} minutos.")

        time.sleep(1)  # Esperar un segundo, simula un minuto en la simulación

    # Mostrar estado de la cola al final de la hora
    print("\nEstado de cola al final de la hora:")
    print(f"Cantidad de clientes en la cola: {cola.qsize()}")
    for i in range(4):
        estado = "Ocupada" if cajas[i] else "Disponible"
        print(f"Caja {i+1}: {estado}")

# Simulación
for hora in range(8):
    num_clientes = np.random.poisson(lmbda)
    momentos_llegada = sorted(np.random.choice(60, num_clientes, replace=False).tolist())  # Minutos aleatorios de llegada
    atender_clientes(hora, momentos_llegada)