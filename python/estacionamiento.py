
import math


class Estacionamiento:
    TARIFA_BOLETO_PERDIDO = 300.0

    def calcular_total(self, minutos: int, tipo_cliente: str = "normal",
                       boleto_perdido: bool = False) -> float:
        
        if minutos < 0:
            raise ValueError("Los minutos no pueden ser negativos")

        if tipo_cliente not in ("normal", "frecuente"):
            raise ValueError("Tipo de cliente no válido")

        if boleto_perdido:
            total = self.TARIFA_BOLETO_PERDIDO
        elif minutos <= 15: #se añadió un =, pues el cobro empieza a ser desde los 16 minutos, no desde los 15.
            total = 0.0
        elif minutos <= 60:
            total = 20.0
        else:
            horas = minutos // 60 #¿cuantas horas tengo?
            if minutos % 60 != 0: #si los minutos no son "exactos", es decir, si no son exactamente multiplo de 60
                horas += 1

            total = 20.0 + ((horas - 1) * 15.0) #le quitamos 1 hora, porque esa ya se cobró de cierta manera y solo ocupamos que
                                                #se empiece a cobrar a partir de los 61 minutos otra hora, de los 121 otra y asi sucesivamente

        if tipo_cliente == "frecuente":
            total *= 0.90

        return round(total, 2)
