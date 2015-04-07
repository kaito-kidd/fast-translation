#!/usr/bin/env python
# -*- coding: utf8 -*-

"""翻译基类

词典解析和翻译解析都继承于此类。
"""

# sys
import sys
import urllib2
import json


class NotImplementedError(Exception):

    """ 未实现异常 """

    def __init__(self, method_name):
        super(NotImplementedError, self).__init__()
        self.method_name = method_name

    def __str__(self):
        return "%s method not implemented!" % self.method

    __repr__ = __str__


class Parser(object):

    """ 翻译基类 """

    BASE_URL = None
    API_KEY = "GM3N6zSue8SvSFU7xhWTZPQ9"

    def __init__(self, input_args, from_="auto", to="auto", args_errmsg=None):
        self.from_ = from_
        self.to = to
        self.timeout = 10
        if len(input_args) != 2:
            print 'Error: %s' % args_errmsg or "Enter a word!"
            sys.exit(1)
        self.word_or_sentence = self.parse_args(input_args)
        self.translate()

    def parse_args(self, input_args):
        """解析命令
        """
        raise NotImplementedError("parse_args")

    def translate(self):
        """翻译
        """
        # 构建URL和参数
        url, data = self.build_url_params()
        try:
            response = urllib2.urlopen(
                url, data=data, timeout=self.timeout)
            if response.code != 200:
                print "Error: Network error %s" % response.code
                sys.exit(1)
            content = response.read()
        except urllib2.HTTPError as exc:
            print "Error: %s" % str(exc)
            sys.exit(1)
        res = json.loads(content)
        self.parse_result(res)

    def build_url_params(self):
        """构建请求参数
        """
        raise NotImplementedError("build_url_params")

    def parse_result(self, res):
        """解析结果
        """
        raise NotImplementedError("parse_result")
