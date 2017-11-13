from bs4 import BeautifulSoup


class Result(object):
    '''结果验证'''

    def __init__(self, result='pass'):
        self.result = result

    def assert_wrong_data(self, html_text, test_data):
        if html_text == '':
            print('测试数据： {}'.format(test_data))
            print('[pass] 没有返回html')
            print('\n')
        elif html_text == "SUCCESS":
            print('测试数据： {}'.format(test_data))
            print('[fail] 返回的html:'+html_text)
            self.result = 'fail'
            print('\n')

        elif 0< len(html_text) <100:
            print('测试数据： {}'.format(test_data))
            print('[pass] 返回的html:' + html_text)
            print('\n')

        elif len(html_text) >100:
            soup = BeautifulSoup(html_text, 'html.parser')
            result_errmsg = soup.find_all('input', attrs={"id": "errMsg"})[0]['value']
            if result_errmsg == '':
                print('测试数据： {}'.format(test_data))
                print('errMsg: {}'.format(result_errmsg))
                print('[fail] 缺少errMsg')
                self.result = 'fail'
                print('\n')

            else:
                print('测试数据： {}'.format(test_data))
                print('[pass] errMsg: {}'.format(result_errmsg))
                print('\n')

    def assert_right_data(self, html_text, test_data):
        if html_text == '':
            print('测试数据： {}'.format(test_data))
            print('[fail] 没有返回html')
            self.result = 'fail'
            print('\n')

        elif html_text == "SUCCESS":
            print('测试数据： {}'.format(test_data))
            print('[pass] 返回的html：'+html_text)
        else:
            soup = BeautifulSoup(html_text, 'html.parser')
            result_errmsg = soup.find_all('input', attrs={"id": "errMsg"})[0]['value']
            if result_errmsg != '':
                print('[fail] 不应该有errMsg')
                self.result = 'fail'
                print('\n')
            else:
                print('测试数据： {}'.format(test_data))
                print('[pass] errMsg: {}'.format(result_errmsg))

    def make_result(self):
        assert self.result == 'pass'

if __name__ == '__main__':
    pass