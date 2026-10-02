
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


#a partir de aquí estan los casos con entradas inválidas
def test_caso_invalido(sistema):
    minutos = -1
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "normal", False) 


#aqui deben de ir casos parametrizados
# 
#     


#a partir de aquí, hay casos con interacciones entre reglas.
def test_caso_cliente_frecuente16(sistema):
    minutos = 16
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    assert resultado == 18.00 #no se utiliza .aprox, pues es algo entero todavía




# TODO:
# 1. Agregue casos normales.
# 2. Agregue casos frontera.
# 3. Agregue entradas inválidas con pytest.raises.
# 4. Agregue casos parametrizados con @pytest.mark.parametrize.
# 5. Use pytest.approx cuando el resultado esperado tenga decimales.
# 6. Pruebe interacciones entre reglas.
