from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/password.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('password')

def tearDownModule():
    mysql.db_close()

class Password(unittest.TestCase):

    #@unittest.skip('')
    def test_password(self):
        data = mysql.db_select('common')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'oldPassword': 'password',
                    'newPassword': 'password',
                    'reNewPassword': val[0],
                    'ACTION': ''}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
