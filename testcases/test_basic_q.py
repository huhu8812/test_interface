from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/Basic8021q.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('802.1q_basic')

def tearDownModule():
    mysql.db_close()

class Basic_Q(unittest.TestCase):

    #@unittest.skip('')
    def test_basic_q(self):
        '''Basic 802.1q 端口vlan id设置'''
        data = mysql.db_select('vlanGroupID')

        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'status': 'Enable',
                    'port1': '1',
                    'port2': '4',
                    'port3': '3',
                    'port4': '1',
                    'port5': '1',
                    'port6': '1',
                    'port7': '1',
                    'port8': '1',
                    'port9': '1',
                    'port10': '1',
                    'port11': '1',
                    'port12': '1',
                    'vlanGroupID': val[0],
                    'ACTION': ''}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
