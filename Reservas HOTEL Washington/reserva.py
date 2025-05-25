from datetime import datetime, time
from comprobante import Comprobante


HORARIOS_VALIDOS = {
    "mañana": (time(8, 0), time(12, 0)),
    "tarde": (time(14, 0), time(18, 0)),
    "noche": (time(20, 0), time(23, 59))
}

class Reserva:
    def __init__(self, habitacion_num, cliente, fecha, hora_inicio, monto=50):
        self.habitacion_num = habitacion_num
        self.cliente = cliente
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.monto = monto
        self.comprobante = None ##funcion nueva del comprobante(extra)

    def es_valida(self):
        try:
            hora = datetime.strptime(self.hora_inicio, "%H:%M").time()
            return any(inicio <= hora <= fin for inicio, fin in HORARIOS_VALIDOS.values())
        except ValueError:
            return False

    def generar_comprobante(self):
        self.comprobante = Comprobante(self.cliente, self.habitacion_num, self.fecha, self.hora_inicio, self.monto)
