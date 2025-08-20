import os

# Caminho absoluto para o arquivo CSV
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'posts.csv'))

def read_csv() -> list:
    posts = []

    arq = open(csv_path, 'r', encoding='utf-8')
    dados = arq.read().splitlines()
    arq.close()

    for i in range(1, len(dados)):
        title, *content = dados[i].split(',')
        posts.append({
            "title": title, 
            "content": ", ".join(content)
        })
    
    return posts

def overwrite_csv(posts: list) -> None:
    arq = open(csv_path, 'w', encoding='utf-8')

    conteudo = ["TITLE,CONTENT"]

    for post in posts:
        conteudo.append(f"{post["title"]},{post["content"]}")
    
    arq.write(f"{"\n".join(conteudo)}\n")
    
    arq.close()

def write_csv(title: str, content: str) -> None:
    arq = open(csv_path, 'a', encoding='utf-8')

    arq.write(f"{title},{content}\n")

    arq.close()