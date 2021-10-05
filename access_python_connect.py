import pyodbc

conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\AutoShop\w_orders.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Orders')

for row in cursor.fetchall():
    print(row)
