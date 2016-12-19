from .tipo import TipoRecurso

class Recurso():
    def __init__(self, nome, tipo, local, agendamentos=[], utilizavel=True, id=None):
        self.id = id
        self.nome = nome
        self.local = local
        self.tipo = tipo
        self.agendamentos = agendamentos
        self.utilizavel = utilizavel
