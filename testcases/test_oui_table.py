from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/voice_vlan_oui.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('voice vlan')

def tearDownModule():
    mysql.db_close()

class OUI_Table(unittest.TestCase):

    #@unittest.skip('')
    def test_Description(self):
        data = mysql.db_select('Description')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'TELT_OUI':'00:01:e3',
                    'TELT_OUI_CHK':'00:01:e3',
                    'DESCRIPTION':val[0],
                    'ACTION':'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    #@unittest.skip('')
    def test_Telt_OUI(self):
        data = mysql.db_select('common')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'TELT_OUI':val[0],
                    'TELT_OUI_CHK':'00:01:e3',
                    'DESCRIPTION':'test',
                    'ACTION':'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()


if __name__ == '__main__':
    unittest.main()
