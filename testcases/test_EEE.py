from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/powerSaving.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('eee')

def tearDownModule():
    mysql.db_close()

class PowerSaving(unittest.TestCase):

    #@unittest.skip('')
    def test_power_saving(self):
        '''power saving状态测试'''
        data = mysql.db_select('eee_status')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'eee_status': val[0],
                    'ACTION': ''}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
