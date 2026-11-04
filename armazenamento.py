import json
import os


CAMINHO = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "dados.json"
)




class Armazenamento:


    @staticmethod
    def carregar():
        os.makedirs(os.path.dirname(CAMINHO), exist_ok=True)


        if not os.path.exists(CAMINHO):
            Armazenamento.salvar({
                "clientes": [],
                "produtos": [],
                "pedidos": [],
                "reclamacoes": [],
                "atendimentos": []
            })


        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)


    @staticmethod
    def salvar(dados):
        os.makedirs(os.path.dirname(CAMINHO), exist_ok=True)


        temporario = CAMINHO + ".tmp"


        with open(temporario, "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )
