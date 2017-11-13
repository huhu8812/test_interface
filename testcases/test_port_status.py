from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/port_settings.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('port status')

def tearDownModule():
    mysql.db_close()

class PortStatus(unittest.TestCase):
    #@unittest.skip('跳过')
    def test_wrong_port_name(self):
        data = mysql.db_select('wrong_port_name')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'PORT_NO': '1;2;3;4;5;6;7;8;9;10;11;12;',
                    'PORT_DESCRIPTION': val[0],
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    #@unittest.skip('跳过')
    def test_right_port_name(self):
        data = mysql.db_select('right_port_name')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'PORT_NO': '1;2;3;4;5;6;7;8;9;10;11;12;',
                    'PORT_DESCRIPTION': val[0],
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_right_data(http.response(), val[0])
        r.make_result()

    #@unittest.skip('ii')
    def test_port_speed(self):
        data = mysql.db_select('port_ctrl_speed')
        r = assert_result.Result()
        for val in data:
            form = { 'Gambit': common_config.gambit,
                     'PORT_NO': '11;12;',
                     'PORT_CTRL_MODE': '2',  # PORT_CTRL_MODE: 1-Auto, 2-force, 3-disable
                     'PORT_CTRL_DUPLEX': '2', # PORT_CTRL_DUPLEX: 1-Full, 2-half
                     'PORT_CTRL_SPEED': val[0], # PORT_CTRL_SPEED: 0-no speed, 1-10M, 2-100M
                     'FLOW_CONTROL_MODE': '4', # FLOW_CONTROL_MODE: 1-disable, 4-enable
                     'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    #@unittest.skip('跳过')
    def test_flow_control(self):
        data = mysql.db_select('port_ctrl_speed')
        r = assert_result.Result()
        for val in data:
            form = { 'Gambit': common_config.gambit,
                     'PORT_NO': '11;12;',
                     'PORT_CTRL_MODE': '1',  # PORT_CTRL_MODE: 1-Auto, 2-force, 3-disable
                     'PORT_CTRL_DUPLEX': '2', # PORT_CTRL_DUPLEX: 1-Full, 2-half
                     'PORT_CTRL_SPEED': '2', # PORT_CTRL_SPEED: 0-no speed, 1-10M, 2-100M
                     'FLOW_CONTROL_MODE': val[0], # FLOW_CONTROL_MODE: 1-disable, 4-enable
                     'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
