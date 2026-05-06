from datetime import datetime

gastos = []

def agregar_gasto():
    monto = float(input("💸 Monto: "))
    categoria = input("📂 Categoría: ")
    fecha = input("📅 Fecha (YYYY-MM-DD): ")
    
    gastos.append({
        "monto": monto,
        "categoria": categoria,
        "fecha": datetime.strptime(fecha, "%Y-%m-%d")
    })

def mostrar_gastos():
    print("\n📋 LISTA DE GASTOS")
    print("-" * 30)
    for g in gastos:
        print(f"{g['fecha'].date()} | {g['categoria']} | ${g['monto']}")
    print("-" * 30)

def total_gastos():
    total = sum(g["monto"] for g in gastos)
    print(f"\n💰 Total gastado: ${total}")

def gastos_por_semana():
    semanas = {}

    for g in gastos:
        semana = g["fecha"].isocalendar()[1]
        semanas.setdefault(semana, 0)
        semanas[semana] += g["monto"]

    print("\n📊 GASTOS POR SEMANA")
    for semana, total in sorted(semanas.items()):
        print(f"Semana {semana}: ${total}")

    # Comparar semanas
    semanas_lista = sorted(semanas.items())
    print("\n📈 COMPARACIÓN:")
    for i in range(1, len(semanas_lista)):
        semana_actual, gasto_actual = semanas_lista[i]
        semana_anterior, gasto_anterior = semanas_lista[i-1]

        diferencia = gasto_actual - gasto_anterior

        if diferencia > 0:
            print(f"🔺 Semana {semana_actual}: gastaste ${diferencia} MÁS que la anterior")
        else:
            print(f"🔻 Semana {semana_actual}: gastaste ${abs(diferencia)} MENOS que la anterior")

# Menú simple
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Total gastado")
    print("4. Ver análisis semanal")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        mostrar_gastos()
    elif opcion == "3":
        total_gastos()
    elif opcion == "4":
        gastos_por_semana()
    elif opcion == "5":
        break
