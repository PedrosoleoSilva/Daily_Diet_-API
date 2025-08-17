from flask import Flask, request, jsonify
from models.dieta import Diet

app = Flask(__name__)

diets = []
id_diet = 1

@app.route("/diet", methods=["POST"])
def create_diet():
    global id_diet
    data = request.get_json()
    nova_diet = Diet(id = id_diet, nome = data.get("nome"), descricao = data.get("descricao"))
    id_diet += 1
    diets.append(nova_diet)
    print(nova_diet)
    return jsonify({"message": "Dieta criada com sucesso!"})

@app.route("/diet", methods=["GET"])
def list_diet():
    list_diet = [diet.to_dict()  for diet in diets]
    output = {
        "Dieta": list_diet
    }
    return jsonify(output)

@app.route("/diet/<int:id>", methods=["GET"])
def listar_diet(id):
    for d in diets:
        if d.id == id:
            return jsonify(d.to_dict())
    return jsonify({"message": "Não foi possivel encontrar a dieta"}), 404

@app.route("/diet/<int:id>", methods=["PUT"])
def update_diet(id):
    diet = None
    for d in diets:
        if d.id == id:
            diet = d
            break
    return jsonify({"message": "Elemento não encontrado"}), 404 
    data = request.get_json()
    diets.nome = data["nome"]
    diet.descricao = data["descricao"]
    return jsonify({"message": "Dieta atualizada com sucesso!"})

@app.route("/diet/<int:id>", methods=["DELETE"])
def deletar_diet(id):
    diet = None
    for d in diets:
        if d.id == id:
            diet = d
            break
    return jsonify({"message": "Não foi possivel encontrar a dieta"}), 404
    diets.remove(diet)
    return jsonify({"message": "Dieta deletada com sucesso!"})
if __name__ == "__main__":
    app.run(debug=True)