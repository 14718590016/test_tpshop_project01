# 导包
import pymysql

# 建立连接（基本都是固定语法）,,pymysql中的编码没有-的，，如下utf8
conn = pymysql.connect(host='localhost', user='root', password='root', database='tpshop2.0', charset='utf8')
# pymysql一般只能通过执行查询语句，才能打印结果 并且打印的方式，不是接收返回值。
cursor = conn.cursor()
cursor.execute("select mobile from tp_users where mobile=14718512347")
# cursor.rownumber=0
print("第一本书是： ", cursor.fetchone()[0])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

