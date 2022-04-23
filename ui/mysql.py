from PyQt5.QtSql import QSqlDatabase

db = QSqlDatabase.addDatabase('QMYSQL')
db.setHostName('localhost')
db.setPort(3306)
db.setDatabaseName('username')
db.setUserName('root')
db.setPassword('123456')
if db.open():
     print("连接成功")
else:
     print("连接失败")
