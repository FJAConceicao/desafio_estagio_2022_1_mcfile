#!/usr/bin/env python3

from github import Github

# Função para exibir as informações solicitadas do repositório
def print_repo_details(repository):
    
    print(f"Nome do repositório: {str(repository.full_name)}")
    print(f"Descrição do repositório: {str(repository.description)}")
    print(f"Nome do autor: {str(repository.owner.name)}")
    print(f"Linguagem do repositório: {str(repository.language)}")
    print(f"Número de Stars: {repository.stargazers_count}")
    print(f"Número de Forks: {repository.forks}")

    date_in_str = repository.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Data da última atualização: {date_in_str}")
    
    print("-"*50 + "\n")

# Conecta ao github por meio de token
token = "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"
github = Github(token)

# Captura termo de consulta e efetua busca
name_to_search = input("Entre com o nome do reposlsitório para busca: ")
repositories_found = github.search_repositories(name_to_search, sort="stars", order="desc")

# Itera por cada repositório encontrado e mostra detalhes de cada um deles
for repository in repositories_found:
    print_repo_details(repository)