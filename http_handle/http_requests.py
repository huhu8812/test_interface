import requests
from bs4 import BeautifulSoup

class HttpHandle(object):
    '''处理http请求类'''
    def __init__(self, url, form):
        self.url = url
        self.form = form

    def _request_post(self):
        # 发出post请求
        return requests.post(self.url, self.form)

    def response(self):
        r = self._request_post()
        return r.text

