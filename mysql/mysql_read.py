import pymysql
import configparser as cparser
import os

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== MySql base operating ===================
class Mysql(object):
    def __init__(self, db):
        #连接mysql
        self.conn = pymysql.connect(host=host, port=int(port), user=user, passwd=password, db = db, charset='utf8')
        #创建游标
        self.cursor = self.conn.cursor()

    def db_select(self, form_data):
        #从mysql中取出数据
        self.cursor.execute('select {0} from {1}'.format(form_data, form_data))
        data = self.cursor.fetchall()
        return data

    def  db_close(self):
        # 关闭数据库
        self.conn.close()

if __name__ == '__main__':
    #test
    m = Mysql('802.1q_advanced_pvidsetting')
    print(m.db_select('wrong_pvid'))
