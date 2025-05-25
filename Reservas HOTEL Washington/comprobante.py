from datetime import datetime

class Comprobante:
    def __init__(self, cliente, habitacion_num, fecha, hora_inicio, monto):
        self.cliente = cliente
        self.habitacion_num = habitacion_num
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.monto = monto
        self.fecha_emision = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"📄 COMPROBANTE DE PAGO\n"
            f"Cliente: {self.cliente}\n"
            f"Habitación: {self.habitacion_num}\n"
            f"Fecha reserva: {self.fecha}\n"
            f"Hora: {self.hora_inicio}\n"
            f"Monto: ${self.monto:.2f}\n"
            f"Fecha de emisión: {self.fecha_emision}\n"
        )
