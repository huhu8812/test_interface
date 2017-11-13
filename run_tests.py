import time, sys
sys.path.append('./testcases')
sys.path.append('./config')
from HTMLTestRunner import HTMLTestRunner
import unittest
from send_email import email_report



# 指定测试用例为当前文件夹下的 interface 目录
test_dir = 'D:\\interface_test\\test_interface\\testcases'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir)


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Switch Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()

    #发送邮件
    testMail = email_report.SendEmail('MINGYUAN.HU@DELTAWW.COM')
    testMail.send_report('D:\interface_test\\test_interface\\report')
