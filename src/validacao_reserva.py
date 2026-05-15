from abc import ABC, abstractmethod
from datetime import datetime
from usuario import Professor
from sala import Laboratorio

#corrente
class ValidadorReserva(ABC):
    def __init__(self):
        self.proximo = None

    def definir_proximo(self, proximo):
        self.proximo = proximo
        return proximo

    @abstractmethod
    def validar(self, usuario, sala, inicio, fim) -> bool:
        if self.proximo:
            return self.proximo.validar(usuario, sala, inicio, fim)
        return True

#reservas no passado
class ValidadorHorarioFuturo(ValidadorReserva):
    def validar(self, usuario, sala, inicio, fim) -> bool:
        if inicio < datetime.now():
            print(f"{usuario.nome}, não é possível reservar horários no passado.")
            return False
        return super().validar(usuario, sala, inicio, fim)

#alunos/externos reservem laboratórios devem ser impedidos
class ValidadorPermissaoLaboratorio(ValidadorReserva):
    def validar(self, usuario, sala, inicio, fim) -> bool:
        if isinstance(sala, Laboratorio) and not isinstance(usuario, Professor):
            print(f"{usuario.nome}, apenas professores podem reservar o laboratório {sala.numero_sala}.")
            return False
        return super().validar(usuario, sala, inicio, fim)