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



if __name__ == "__main__":
    app.run(debug=True)