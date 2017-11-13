import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os, time

class SendEmail(object):
    def __init__(self, receiver):
        self.receiver = receiver

    def send_mail(self, file_new):
        msg = MIMEMultipart()
        #定义标题
        msg['Subject'] = u"Web接口自动化测试报告"
        #定义发送时间（有些邮件客户端可能不显示发送时间）
        msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        #构造附件
        att = MIMEText(open(file_new, 'rb').read(), 'base64', _charset='utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=%s' % self.newReport
        msg.attach(att)

        smtp = smtplib.SMTP()
        #连接smtp服务器
        smtp.connect('CNDGCCAS01.delta.corp')
        #用户名和密码
        smtp.login('mingyuan.hu', 'Delta0770')
        smtp.sendmail('MINGYUAN.HU@DELTAWW.COM', self.receiver, msg.as_string())
        smtp.quit()

    #找到最新的测试报告并发送
    def send_report(self, testReport):
        result_dir = testReport
        lists = os.listdir(result_dir)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))

        self.newReport = lists[-1]

        #最新生成的报告
        file_new = os.path.join(result_dir, self.newReport)
        print(file_new)

        self.send_mail(file_new)




