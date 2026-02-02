import mysql.connector
cnx = mysql.connector.connect(host='localhost',database='db_teste',user='root',password='Anninha16!')

if cnx.is_connected():
    db_info = cnx.get_server_info()
    print("Conectado ao servidor MySQL versão",db_info)
    cursor = cnx.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)

if cnx.is_connected():
    cursor.close()
    cnx.close()
    print("Conexão ao MySQL foi encerrada")
