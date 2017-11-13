from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/lag_settings.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('lag configuration')

def tearDownModule():
    mysql.db_close()

class LagConfiguration(unittest.TestCase):

    #@unittest.skip('')
    def test_wrong_lag_name(self):
        data = mysql.db_select('wrong_lag_name')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'PORT_NO': '1;',
                    'LAG_NAME': val[0], #512 lag name只能输入字母，数字，-，_
                    'ADMIN_STATUS': 'disable', #1 --> enable, 2 --> disable, 0 --> 空白
                    'LAG_TYPE': '1', # 1 --> static, 2 --> lacp, 0 --> 空白
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    # @unittest.skip('')
    def test_right_lag_name(self):
        data = mysql.db_select('right_lag_name')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'PORT_NO': '1;',
                    'LAG_NAME': val[0],
                    # 512 lag name只能输入字母，数字，-，_
                    'ADMIN_STATUS': 'disable',  # 1 --> enable, 2 --> disable, 0 --> 空白
                    'LAG_TYPE': '1',  # 1 --> static, 2 --> lacp, 0 --> 空白
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

        # @unittest.skip('')
        def test_lag_configuration(self):
            data = mysql.db_select('common')
            r = assert_result.Result()
            for val in data:
                form = {'Gambit': common_config.gambit,
                        'PORT_NO': '1;',
                        'LAG_NAME': 'test', # 512 lag name只能输入字母，数字，-，_
                        'ADMIN_STATUS': val[0],  # 1 --> enable, 2 --> disable, 0 --> 空白
                        'LAG_TYPE': val[0],  # 1 --> static, 2 --> lacp, 0 --> 空白
                        'ACTION': 'Apply'}

                http = http_requests.HttpHandle(url, form)
                r.assert_wrong_data(http.response(), val[0])
            r.make_result()

if __name__ == '__main__':
    unittest.main()
