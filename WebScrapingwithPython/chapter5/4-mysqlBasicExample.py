import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='mysql07', db='mysql')

cur = conn.cursor()
cur.execute('USE dsc')
cur.execute('select * from course')
print(cur.fetchone())
print(cur.fetchone())
cur.close()
conn.close()