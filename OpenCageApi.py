# Codigo Python para pegar a latitude e longitude de endereços de tabelas do SqlServer atraves da API OpenCage
#
from geopy.geocoders import OpenCage
opencage = OpenCage('suaApiGeradaNoSiteOpenCage.com', domain='api.opencagedata.com', scheme='https', timeout=None, proxies=None, user_agent=None)
import pypyodbc as pyodbc

#Faz a conexão com o banco do Sql Server
connection = 'Driver={SQL Server};Server=10.x.x.x;Database=nomeDatabase;UID=user;PWD=123'
db = pyodbc.connect(connection)


cursor = db.cursor()
cursor.execute('select endereco from cadastro')

for row in cursor.fetchall():
    localizacao = list(opencage.geocode(row,exactly_one=True))[1]
    print(localizacao)


