from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/port_ratectrl.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('rate limit')

def tearDownModule():
    mysql.db_close()

class RateLimit(unittest.TestCase):

    #@unittest.skip('')
    def test_rateLimit(self):
        data = mysql.db_select('rate')
        r = assert_result.Result()
        for val in data:
            form = {  'Gambit': common_config.gambit,
                      'issExtRateCtrlIndex': '4;5;',
                      'issExtRateCtrlPortIngressRateLimit': val[0],
                      'issExtRateCtrlPortEgressRateLimit': val[0],
                      'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
