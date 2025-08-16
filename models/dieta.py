from datetime import datetime
class Diet:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.data_hora = datetime.now()

    def to_dict(self):
        return {
                    "id": self.id,
                    "nome": self.nome,
                    "descricao": self.descricao,
                    "data_hora": self.data_hora.strftime("%Y-%m-%d %H:%M:%S")
                }
        