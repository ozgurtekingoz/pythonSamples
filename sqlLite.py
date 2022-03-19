import sqlite3

con = sqlite3.connect("deneme.db")

cursor = con.cursor()


def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS musteriler(ad TEXT,SOYAD TEXT,TCKN INT)")


def insertTable():
    cursor.execute("INSERT INTO musteriler values ('bilge','köse',22222222)")
    con.commit()


def selectTable():
    cursor.execute("select * from musteriler")
    data = cursor.fetchall()
    for item in data:
        print(item)


def updateTable():
    cursor.execute("UPDATE musteriler SET SOYAD ='DENEME' WHERE TCKN=22222222")
    con.commit()


# createTable()
# insertTable()
#updateTable()
selectTable()
con.close()
