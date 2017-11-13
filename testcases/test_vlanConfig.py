from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/Cf8021q.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('802.1q_vlan config')

def tearDownModule():
    mysql.db_close()

class Q_VlanConfig(unittest.TestCase):

    #@unittest.skip('')
    def test_wrong_vlanID(self):
        data = mysql.db_select('add_vlanid_wrong')
        r = assert_result.Result()
        for val in data:
            form = {  'Gambit': common_config.gambit,
                      'status': 'Enable',
                      'ADD_VLANID': val[0],
                      'selectedVLANs': '2;3;',
                      'ACTION':  'add'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    # @unittest.skip('')
    def test_action(self):
        data = mysql.db_select('action')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'status': 'Enable',
                    'ADD_VLANID': '2',
                    'selectedVLANs': '2;3;',
                    'ACTION': val[0]}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
