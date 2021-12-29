import psycopg2 as pg2

dbConnection = pg2.connect(database = 'dvdrental', user= 'postgres', password = 'YOUR PASSWORD')
cursor = dbConnection.cursor()
cursor.execute('SELECT * FROM film')
print(cursor.fetchmany(10))
dbConnection.close()