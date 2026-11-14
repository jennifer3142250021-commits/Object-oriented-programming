class SuscripcionExpiradaError(Exception):
    #it will be launch when a user tries to use a function
    #without an active sucription
    pass
class PuntosInsuficientesError(Exception): 
    #raised when a transiction exceeds
    #the availble gem balance 
    pass

class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50):
        if gemas < 0:
            raise ValueError("Las gemas iniciales no pueden ser negativas.")
        self.username = username
        self.gemas = gemas
        self.racha_dias = 1
        self.notificaciones_activas = True

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad a ganar debe ser mayor a 0.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad a gastar debe ser mayor a 0.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No tienes gemas suficientes.")
        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(self, username: str, gemas: int = 50, meses_suscripcion: int = 1):
        super().__init__(username, gemas)
        if meses_suscripcion <= 0:
            raise ValueError("Los meses de suscripción deben ser mayores a 0.")
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0 or not self.es_pro:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción Pro ha expirado.")
        return "Descarga iniciada con éxito."