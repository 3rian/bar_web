from flask import Flask, render_template, request

app = Flask(__name__)
cervejas = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        marca = request.form["marca"]
        quantidade = int(request.form["quantidade"])
        preco = float(request.form["preco"])
        
        if marca not in cervejas:
            cervejas[marca] = {"quantidade": 0, "preco": preco}
        cervejas[marca]["quantidade"] += quantidade
        cervejas[marca]["preco"] = preco

    total_geral = sum(d["quantidade"] * d["preco"] for d in cervejas.values())
    return render_template("index.html", cervejas=cervejas, total_geral=total_geral)

if __name__ == "__main__":
    app.run(debug=True)
