import json
from reserva import Reserva
from datetime import datetime

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = [i for i in range(1, 6)]  # habitaciones 1 a 5
        self.reservas = []
        self.cargar_reservas()

    def crear_reserva(self, reserva):
        if not reserva.es_valida():
            print("⛔ Horario inválido.")
            return False

        if self.esta_disponible(reserva.habitacion_num, reserva.fecha, reserva.hora_inicio):
            reserva.generar_comprobante()
            self.reservas.append(reserva)
            self.guardar_reservas()

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nombre_archivo = f"comprobante_{reserva.cliente.lower().replace(' ', '_')}_{reserva.fecha}_{timestamp}.txt"
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write(str(reserva.comprobante))

            print("✅ Reserva realizada correctamente.")
            print(reserva.comprobante)
            return True
        else:
            print("⛔ Esa habitación ya está reservada en ese horario.")
            return False

    def esta_disponible(self, hab_num, fecha, hora):
        for r in self.reservas:
            if r.habitacion_num == hab_num and r.fecha == fecha and r.hora_inicio == hora:
                return False
        return True

    def guardar_reservas(self):
        with open("reservas.json", "w") as f:
            json.dump(
                [{k: v for k, v in r.__dict__.items() if k != "comprobante"} for r in self.reservas],
                f,
                indent=4
            )

    def cargar_reservas(self):
        try:
            with open("reservas.json", "r") as f:
                data = json.load(f)
                for r in data:
                    self.reservas.append(Reserva(**r))
        except FileNotFoundError:
            self.reservas = []

    def buscar_reservas_por_cliente(self, nombre):
        return [r for r in self.reservas if r.cliente.lower() == nombre.lower()]
