
import pytest

from estacionamiento import Estacionamiento


@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Estacionamiento() # instancia de la clase estacionamiento.

def test_ejemplo_inicial(sistema): #que termina siendo un caso normal
    minutos = 0
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 0.0


#en esta parte se encuentran solo los casos normales
def test_caso_normal1(sistema):
    minutos = 1
    resultado = sistema.calcular_total(minutos, "normal", False)

def test_caso_normal14(sistema):
    minutos = 14
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 0.0

def test_caso_normal17(sistema):   
    minutos = 17
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 20.00


#en esta parte están los casos frontera    
def test_caso_frontera15(sistema):
    minutos = 15
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 0.0

def test_caso_frontera16(sistema):
    minutos = 16
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 20.00

def test_caso_frontera60(sistema):
    minutos = 60
    resultado = sistema.calcular_total(minutos, "normal", False)  
    assert resultado == 20.00

def test_caso_frontera61(sistema):
    minutos = 61
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 35.00

def test_caso_frontera120(sistema):
    minutos = 120
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 35.00

def test_caso_frontera121(sistema):
    minutos = 121
    resultado = sistema.calcular_total(minutos, "normal", False)
    assert resultado == 50.00        


# pruebas de casos con entradas inválidas
def test_caso_invalido_minutos_negativo(sistema):
    minutos = -1
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "normal", False) 

def test_caso_invalido_tipo_cliente(sistema):
    minutos = 0
    tipo_cliente = "especial"
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, tipo_cliente, False)

# pruebas de casos con interacciones entre reglas.
def test_caso_cliente_frecuente16(sistema):
    minutos = 16
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    assert resultado == 18.00 #no se utiliza .aprox, pues es algo entero todavía

def test_caso_cliente_frecuente_boleto_perdido(sistema):
    minutos = 10
    tipo_cliente = "frecuente"
    resultado = sistema.calcular_total(minutos, tipo_cliente, True)
    assert resultado == 300.00
    
# prueba utilizando pytest.aprox cuando el resultado es decimal.
def test_caso_con_decimal(sistema):
    minutos = 181
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    assert resultado == pytest.approx(58.5)

# USO DE PARAMETRIZE: casos normales y casos frontera
@pytest.mark.parametrize(
    "minutos, esperado",
    [
        (5, 0.00), # caso normal
        (30, 20.00), # caso normal
        (70, 35.00), # caso normal
        (0, 0.00), # caso frontera
        (1, 0.00), # caso frontera
        (15, 0.00), # caso frontera
        (16, 20.00), # caso frontera
        (60, 20.00), # caso frontera
        (61, 35.00), # caso frontera
        (120, 35.00), # caso frontera
        (121, 50.00), # caso frontera
    ]
)
def test_casos_normales_fronteras_validos(sistema, minutos, esperado):
    assert sistema.calcular_total(minutos, "normal", False) == esperado

# USO DE PARAMETRIZE: casos inválidos
@pytest.mark.parametrize("minutos_invalidos", [-10, -100, -20])
def test_casos_invalidos_lanza_error(sistema, minutos_invalidos):
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos_invalidos, "normal", False)
        

