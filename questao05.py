from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    conn = MongoClient(url_conexao)
    col = conn[colecao]
    return col
