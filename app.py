from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import random
import img_randon

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/table_name.db'
db = SQLAlchemy(app)#cursor da base de dados

class Name(db.Model):
    __tablename__ = "table_name"
    id = db.Column(db.Integer, primary_key=True)
    nome_invocador = db.Column(db.String(200))
    nome_campeao = db.Column(db.String(200))
    
with app.app_context():
    db.create_all()#criação das tabelas
    db.session.commit()#executa tarefas


@app.route("/")
def home():
    first_names = None
    nome_invocador = request.args.get("nome_invocador")
    if nome_invocador:
        first_names = db.session.query(Name).filter(Name.nome_invocador.like(nome_invocador)).first()
    return render_template("index.html", first_names = first_names)

@app.route("/your-champ", methods=["POST"])
def criar():
    
    nome_invocador = request.form["conteudo_nome"].lower().strip()
    result = db.session.query(Name).filter(Name.nome_invocador == nome_invocador).first()
    if result == None:
        first_name = Name(nome_invocador=request.form["conteudo_nome"].lower().strip(), nome_campeao=f"{img_randon.list_champ()}") 
        db.session.add(first_name)
        db.session.commit()

    
    
    return redirect(url_for('home', nome_invocador = nome_invocador))
    


if __name__ == "__main__":
    app.run(debug=True)

