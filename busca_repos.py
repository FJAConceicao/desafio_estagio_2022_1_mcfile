from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from github import Github

import random
import sys
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Conecta ao github por meio de token
token = "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"
github = Github(token)

class Repository(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_repo = db.Column(db.String(64))
    descricao = db.Column(db.String(256))
    autor = db.Column(db.String(64))
    language = db.Column(db.String(64))
    star_numbers = db.Column(db.Integer)
    fork_numbers = db.Column(db.Integer)
    date_last_update = db.Column(db.String(64))

db.create_all()

def search_add_repos_in_db(name_to_search="banho"):

    repositories_found = github.search_repositories(name_to_search, sort="stars", order="desc")

    # Deletar BD
    #if(os.path.exists("./db.sqlite")):
    #    os.remove("./db.sqlite")

    for repo in repositories_found:

        text_desc = repo.description[:255] if(len(str(repo.description)) > 255) else repo.description

        repository = Repository(name_repo = repo.full_name,
                                descricao = text_desc, 
                                autor = repo.owner.name, 
                                language = repo.language, 
                                star_numbers = repo.stargazers_count, 
                                fork_numbers = repo.forks, 
                                date_last_update = repo.updated_at.strftime("%Y-%m-%d %H:%M:%S"))

        db.session.add(repository)

    db.session.commit()


@app.route('/')
def index():
    
    search_add_repos_in_db()
    
    repositories = Repository.query
    return render_template('basic_table.html', title='Busca repositórios no github', repos=repositories)

if __name__ == '__main__':
    app.debug = True
    app.run()
