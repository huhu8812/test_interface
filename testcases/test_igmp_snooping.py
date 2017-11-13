from config import common_config
from mysql import mysql_read
from http_handle import http_requests
from result_handle import assert_result
import unittest

def setUpModule():
    #模块测试开始前的准备工作
    global url, mysql
    url = 'http://{}/iss/specific/igs_conf.html'.format(common_config.ip)
    mysql = mysql_read.Mysql('igmp snooping')

def tearDownModule():
    mysql.db_close()

class IgmpSnooping(unittest.TestCase):

    #@unittest.skip('')
    def test_ipHeader(self):
        '''validate IGMPv3 IP Header测试'''
        data = mysql.db_select('ip_header')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit,
                    'VLAN_STATUS': '0', # 0-->不开启任何vlan， 1-->port-based vlan, 3-->802.1q
                    'PORT_BASED_NUM': '12',
                    'GLOBAL_STATUS': '1', # 1 --> 开启igmp, 2 --> 关闭igmp
                    'VLAN_ID_ENABLED': '1', # VLAN ID Enabled for IGMP Snooping
                    'IP_HEADER': val[0], # Validate IGMPv3 IP Header， 1 --> enable, 2 --> disable
                    'UMC_STATUS': '1', #block unknown multicast address 1 --> enable, 2 --> disable
                    'ROUTE_PORT': '2', # 静态路由端口 1 --> auto, 2 --> any, 3 --> static
                    'hiddenMem': '',
                    'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    # @unittest.skip('')
    def test_routePort(self):
        '''route port测试'''
        data = mysql.db_select('routePort')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit, 'VLAN_STATUS': '0',
                    # 0-->不开启任何vlan， 1-->port-based vlan, 3-->802.1q
                    'PORT_BASED_NUM': '12',
                    'GLOBAL_STATUS': '1',  # 1 --> 开启igmp, 2 --> 关闭igmp
                    'VLAN_ID_ENABLED': '1',  # VLAN ID Enabled for IGMP Snooping
                    'IP_HEADER': '1',  # Validate IGMPv3 IP Header, 1 --> enable, 2 --> disable
                    'UMC_STATUS': '1',  # block unknown multicast address 1 --> enable, 2 --> disable
                    'ROUTE_PORT': val[0],  # 静态路由端口 1 --> auto, 2 --> any, 3 --> static
                    'hiddenMem': '', 'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response(), val[0])
        r.make_result()

    # @unittest.skip('')
    def test_block_unknown_address(self):
        '''block unknown multicast address测试'''
        data = mysql.db_select('block_address')
        r = assert_result.Result()
        for val in data:
            form = {'Gambit': common_config.gambit, 'VLAN_STATUS': '0',
                    # 0-->不开启任何vlan， 1-->port-based vlan, 3-->802.1q
                    'PORT_BASED_NUM': '12',
                    'GLOBAL_STATUS': '1',  # 1 --> 开启igmp, 2 --> 关闭igmp
                    'VLAN_ID_ENABLED': '1',  # VLAN ID Enabled for IGMP Snooping
                    'IP_HEADER': '1',  # Validate IGMPv3 IP Header, 1 --> enable, 2 --> disable
                    'UMC_STATUS': val[0],  # block unknown multicast address 1 --> enable, 2 --> disable
                    'ROUTE_PORT': '1',  # 静态路由端口 1 --> auto, 2 --> any, 3 --> static
                    'hiddenMem': '', 'ACTION': 'Apply'}

            http = http_requests.HttpHandle(url, form)
            r.assert_wrong_data(http.response() ,val[0])
        r.make_result()

if __name__ == '__main__':
    unittest.main()
