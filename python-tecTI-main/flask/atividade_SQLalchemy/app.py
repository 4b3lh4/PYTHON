import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy  

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "loja-tech-secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "loja.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) 



class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(60), nullable=False)
    preco = db.Column(db.Float, nullable=False, default=0.0)
    estoque = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Produto {self.id} - {self.nome}>"



with app.app_context():
    db.create_all()


def validar(nome, categoria, preco_str, estoque_str):
    """Retorna (ok, mensagem, preco, estoque)."""
    if not nome or not nome.strip():
        return False, "O nome é obrigatório.", 0.0, 0
    if not categoria or not categoria.strip():
        return False, "A categoria é obrigatória.", 0.0, 0
    try:
        preco = float(preco_str)
    except (TypeError, ValueError):
        return False, "Preço inválido.", 0.0, 0
    if preco <= 0:
        return False, "O preço deve ser maior que zero.", 0.0, 0
    try:
        estoque = int(estoque_str) if estoque_str not in (None, "") else 0
    except (TypeError, ValueError):
        return False, "Estoque inválido.", 0.0, 0
    if estoque < 0:
        return False, "O estoque não pode ser negativo.", 0.0, 0
    return True, "", preco, estoque


@app.route("/")
def listar():
   
    produtos = Produto.query.order_by(Produto.nome).all()
    return render_template("lista.html", produtos=produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()
        preco_str = request.form.get("preco", "0")
        estoque_str = request.form.get("estoque", "0")

        ok, msg, preco, estoque = validar(nome, categoria, preco_str, estoque_str)
        if not ok:
            flash(msg, "erro")
           
            produto = Produto(nome=nome, categoria=categoria,
                              preco=float(preco_str or 0), estoque=int(estoque_str or 0))
            return render_template("formulario.html", produto=produto, acao="cadastrar")

     
        novo = Produto(nome=nome, categoria=categoria, preco=preco, estoque=estoque)
        db.session.add(novo)
        db.session.commit()
        flash("Produto cadastrado com sucesso!", "ok")
        return redirect(url_for("listar"))

    return render_template("formulario.html", produto=None, acao="cadastrar")


@app.route("/editar/<int:produto_id>", methods=["GET", "POST"])
def editar(produto_id):
    
    produto = Produto.query.get_or_404(produto_id)

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()
        preco_str = request.form.get("preco", "0")
        estoque_str = request.form.get("estoque", "0")

        ok, msg, preco, estoque = validar(nome, categoria, preco_str, estoque_str)
        if not ok:
            flash(msg, "erro")
            produto.nome = nome
            produto.categoria = categoria
            return render_template("formulario.html", produto=produto, acao="editar")

        
        produto.nome = nome
        produto.categoria = categoria
        produto.preco = preco
        produto.estoque = estoque
        db.session.commit()
        flash("Produto atualizado!", "ok")
        return redirect(url_for("listar"))

    return render_template("formulario.html", produto=produto, acao="editar")


@app.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir(produto_id):
    produto = Produto.query.get_or_404(produto_id)

    db.session.delete(produto)
    db.session.commit()
    flash("Produto excluído.", "ok")
    return redirect(url_for("listar"))


if __name__ == "__main__":
    app.run(debug=True)
