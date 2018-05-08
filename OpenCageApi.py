from geopy.geocoders import OpenCage
opencage = OpenCage('e5dd1925dee24d7ebb0bdb5ada759600', domain='api.opencagedata.com', scheme='https', timeout=None, proxies=None, user_agent=None)
import pypyodbc as pyodbc

#Faz a conexão com o banco do Sql Server
connection = 'Driver={SQL Server};Server=10.50.1.95;Database=jose;UID=soumais;PWD=sou2017mais'
db = pyodbc.connect(connection)


cursor = db.cursor()
cursor.execute('select top 2500 l.endereco,l.geolocalizacao from localizacoes l')

for row in cursor.fetchall():
    localizacao = list(opencage.geocode(list(row)[0],exactly_one=True))[1]
    print(localizacao)


