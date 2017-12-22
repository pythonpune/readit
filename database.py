import pymysql

con = pymysql.connect(host='localhost', user='demo', password='demo', db='test')

a = con.cursor()

sql = 'SELECT * from form;'
a.execute(sql)

countrow = a.execute(sql)
print("number of rows:", countrow)
data = a.fetchone()
print(data)
