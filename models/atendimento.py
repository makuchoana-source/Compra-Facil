class Atendimento:
    def __init__(self, id, reclamacao_id, resposta):
        self.id = id
        self.reclamacao_id = reclamacao_id
        self.resposta = resposta


    def to_dict(self):
        return {
            "id": self.id,
            "reclamacao_id": self.reclamacao_id,
            "resposta": self.resposta
        }
