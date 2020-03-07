import sqlite3

conexao = None
consulta = None
banco_de_dados = 'db_links.sqlite'

try:
    conexao = sqlite3.connect(banco_de_dados)
    consulta = conexao.cursor()
except:
    print('Erro ao abrir conexão com o banco de dados')


def realiza_query(sql, parametros):
    resultado = []

    consulta.execute(sql, parametros)

    for linha in consulta.fetchall():
        resultado.append(linha)

    return resultado


def buscar(palavra_chave):
    sql = 'SELECT url, h1, p FROM link WHERE h1 like ?;'
    parametros = ('%' + palavra_chave + '%',)

    resultado = realiza_query(sql, parametros)

    quantidade_repeticoes_h1 = 0
    quantidade_repeticoes_p = 0
    quantidade_repeticoes = 0
    ranking = []

    for linha in resultado:
        texto_h1 = linha[1]
        quantidade_repeticoes_h1 = texto_h1.count(palavra_chave)
        texto_p = linha[2]
        quantidade_repeticoes_p = texto_p.count(palavra_chave)
        quantidade_repeticoes = quantidade_repeticoes_h1 + quantidade_repeticoes_p
        ranking.append({linha[0]: quantidade_repeticoes})

    print(ranking)


def main():
    palavra_chave = input('Palavra: ').lower()

    buscar(palavra_chave)

    conexao.close()


if __name__ == "__main__":
    main()
