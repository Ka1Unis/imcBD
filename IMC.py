import mysql.connector

def main():
    # Conecta ao banco de dados
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="imc"
    )

    # Cria um cursor
    cursor = connection.cursor()

    # Coleta os dados do usuário
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em m): "))

    # Calcula o IMC
    IMC = peso / altura ** 2

    # Classifica o IMC
    classificação = ""
    if IMC < 18.5:
        classificação = "Abaixo do peso"
    elif IMC <= 24.9:
        classificação = "Peso normal"
    elif IMC <= 29.9:
        classificação = "Sobrepeso"
    elif IMC <= 34.9:
        classificação = "Obesidade grau I"
    elif IMC <= 39.9:
        classificação = "Obesidade grau II"
    else:
        classificação = "Obesidade grau III"

    # Insere o resultado no banco de dados
    cursor.execute("INSERT INTO imc (peso, altura, imc, classificacao) VALUES (%s, %s, %s, %s)", (peso, altura, IMC, classificação))

    # Salva as alterações no banco de dados
    connection.commit()

    # Fecha a conexão com o banco de dados
    connection.close()

if __name__ == "__main__":
    main()