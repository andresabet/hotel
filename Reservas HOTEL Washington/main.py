from hotel import Hotel
from reserva import Reserva

def mostrar_horarios():
    print("Horarios disponibles:")
    print("1. Mañana (08:00 - 12:00)")
    print("2. Tarde (14:00 - 18:00)")
    print("3. Noche (20:00 - 24:00)")

    opciones = {"1": "08:00", "2": "14:00", "3": "20:00"}
    seleccion = input("Selecciona una opción de horario (1-3): ")
    return opciones.get(seleccion, None)

def solicitar_reserva(hotel):
    nombre = input("Nombre del cliente: ")
    while True:
        fecha = input("Fecha de reserva (YYYY-MM-DD): ")
        try:
            habitacion = int(input("Número de habitación (1 al 5): "))
            if habitacion not in hotel.habitaciones:
                print("❌ Habitación no válida.")
                continue
        except ValueError:
            print("❌ Entrada inválida.")
            continue

        hora = mostrar_horarios()
        if not hora:
            print("❌ Horario no válido.")
            continue

        if hora == "08:00":
            monto = 15.0
        elif hora == "14:00":
            monto = 25.0
        elif hora == "20:00":
            monto = 50.0
        else:
            monto = 0.0

        reserva = Reserva(habitacion, nombre, fecha, hora, monto)
        if hotel.crear_reserva(reserva):
            break  # salir si la reserva se crea con éxito



def consultar_reserva(hotel):
    while True:
        nombre = input("Nombre del cliente: ")
        reservas = hotel.buscar_reservas_por_cliente(nombre)
        if not reservas:
            print("❌ No se encontraron reservas con ese nombre.")
            continue
        print(f"\nReservas de {nombre}:")
        for r in reservas:
            print(f"  Habitación {r.habitacion_num} - Fecha: {r.fecha} - Hora: {r.hora_inicio}")
        break

def main():
    hotel = Hotel("Hotel Python")
    print("\n=== Menú Principal ===")
    print("1. Solicitar reserva")
    print("2. Consultar reserva")

    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        solicitar_reserva(hotel)
    elif opcion == "2":
        consultar_reserva(hotel)
    else:
        print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
