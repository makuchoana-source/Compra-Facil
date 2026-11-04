class Pedido:
    def __init__(self, id, cliente_id, produtos, total):
        self.id = id
        self.cliente_id = cliente_id
        self.produtos = produtos
        self.total = total
        self.status = "Aguardando pagamento"


    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "produtos": self.produtos,
            "total": self.total,
            "status": self.status
        }
