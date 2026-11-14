import pytest
from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError
)

# 1. State Isolation (@pytest.fixture)
@pytest.fixture
def perfil_estandar():
    return PerfilMovil(username="gamer123", gemas=50)

@pytest.fixture
def perfil_pro_valido():
    return PerfilPro(username="pro_gamer", gemas=100, meses_suscripcion=2)


# 2. Structural Integrity and Assertion Tests
def test_atributos_iniciales_perfil_movil(perfil_estandar):
    assert perfil_estandar.username == "gamer123"
    assert perfil_estandar.gemas == 50
    assert perfil_estandar.racha_dias == 1
    assert perfil_estandar.notificaciones_activas is True

def test_transacciones_aritmeticas_gemas(perfil_estandar):
    assert perfil_estandar.ganar_gemas(20) == 70
    assert perfil_estandar.gastar_gemas(30) == 40
    assert perfil_estandar.gemas == 40


# 3. Exception Validation (pytest.raises)
def test_excepcion_puntos_insuficientes(perfil_estandar):
    with pytest.raises(PuntosInsuficientesError):
        perfil_estandar.gastar_gemas(100)

def test_excepcion_suscripcion_expirada():
    perfil = PerfilPro(username="pro_user", gemas=50, meses_suscripcion=1)
    perfil.meses_suscripcion = 0  # Simulamos expiración de suscripción
    with pytest.raises(SuscripcionExpiradaError):
        perfil.descargar_contenido_offline()
    assert perfil.es_pro is False

def test_excepcion_valores_invalidos():
    with pytest.raises(ValueError):
        PerfilMovil(username="user_error", gemas=-10)
    with pytest.raises(ValueError):
        PerfilPro(username="pro_error", meses_suscripcion=0)


# 4. Parameterized Tests (@pytest.mark.parametrize)
@pytest.mark.parametrize("cantidad_ganada, resultado_esperado", [
    (10, 60),
    (50, 100),
    (1, 51),
    (100, 150)
])
def test_ganar_gemas_parametrizado(perfil_estandar, cantidad_ganada, resultado_esperado):
    assert perfil_estandar.ganar_gemas(cantidad_ganada) == resultado_esperado

@pytest.mark.parametrize("cantidad_invalida", [0, -5, -100])
def test_ganar_gemas_limites_invalidos(perfil_estandar, cantidad_invalida):
    with pytest.raises(ValueError):
        perfil_estandar.ganar_gemas(cantidad_invalida)


# 5. Type and Hierarchy Verification (isinstance)
def test_jerarquia_herencia(perfil_pro_valido):
    assert isinstance(perfil_pro_valido, PerfilPro)
    assert isinstance(perfil_pro_valido, PerfilMovil)
    assert perfil_pro_valido.descargar_contenido_offline() == "Descarga iniciada con éxito."
