class Reclamacao:
    def __init__(self, id, cliente_id, pedido_id, assunto, descricao):
        self.id = id
        self.cliente_id = cliente_id
        self.pedido_id = pedido_id
        self.assunto = assunto
        self.descricao = descricao
        self.status = "Em análise"
        self.resposta = None


    def responder(self, resposta):
        self.resposta = resposta
        self.status = "Respondida"


    def resolver(self):
        self.status = "Resolvida"


    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "pedido_id": self.pedido_id,
            "assunto": self.assunto,
            "descricao": self.descricao,
            "status": self.status,
            "resposta": self.resposta
        }
