#!/usr/bin/env python3

from github import Github

# Função para exibir as informações solicitadas do repositório
def print_repo_details(repository):
    
    print(f"Nome do repositório: {repository.full_name}")
    print(f"Descrição do repositório: {repository.description}")
    print(f"Nome do autor: {repository.owner}")
    print(f"Linguagem do repositório: {repository.language}")
    print(f"Número de Stars: {repository.stargazers_count}")
    print(f"Número de Forks: {repository.forks}")
    print(f"Data da última atualização: {repository.updated_at}")
    
    print("-"*50 + "\n")

# Conecta ao github por meio de token
token = "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"
github = Github(password)

# Captura termo de consulta e efetua busca
name_to_search = input("Entre com o nome do repositório para busca: ")
repositories_found = github.search_repositories(name_to_search, sort="stars", order="desc")

