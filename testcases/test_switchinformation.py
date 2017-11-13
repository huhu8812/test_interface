# 导入所需的模块和库
from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule(): # 定义测试用例执行前的初始化工作。
    global url, mysql
    url = 'http://{}/iss/specific/sysInfo.html'.format(common_config.ip) #switch information页面的url
    mysql = mysql_read.Mysql('switch information') # 建立switch information页面的数据库连接

def tearDownModule(): # 定义测试用例执行完成后的测试环境还原工作。
    mysql.db_close()  # 关闭数据库连接

class SwitchInformation(unittest.TestCase):
    #@unittest.skip('') # 给测试用例前添加一个unittest.skip(跳过原因)，可以直接不执行这个case。
    def test_wrong_switch_name(self):
        '''Case1: 测试错误的交换机name输入'''
        data = mysql.db_select('wrong_switch_name') #从数据库中取出name
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit, # switch information页面的form表单
                    'refreshFlag': '0',
                    'dhcp_mode': '2',
                    'switch_name': val[0],  # 这里的val[0]输入的是从数据库中读取的switch name
                    'IP_ADDRESS': '192.168.0.239',
                    'SUBNET_MASK': '255.255.255.0',
                    'GATEWAY_ADDRESS': '192.168.0.254',
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)  # 调用http_handele模块，向dut发送http包
            r.assert_wrong_data(http.response(), val[0]) # 判断测试结果是否通过
        r.make_result()

    def test_right_switch_name(self):
        '''Case2: 测试正确的交换机name输入'''   #原理同上
        data = mysql.db_select('right_switch_name')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'refreshFlag': '1',
                    'dhcp_mode': '2',
                    'switch_name': val[0],
                    'IP_ADDRESS': '192.168.0.239',
                    'SUBNET_MASK': '255.255.255.0',
                    'GATEWAY_ADDRESS': '192.168.0.254',
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_right_data(http.response(), val[0])
        r.make_result()

    #@unittest.skip('ii')
    def test_wrong_ip_address(self):
        '''测试错误的交换机ip地址输入'''
        data = mysql.db_select('wrong_ip_address')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'refreshFlag': '0',
                    'dhcp_mode': '2',
                    'IP_ADDRESS': val[0],
                    'SUBNET_MASK': '255.255.255.0',
                    'GATEWAY_ADDRESS': '192.168.0.254',
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
