#!/usr/bin/env python
# -*- coding: utf8 -*-

"""基于命令行的快速翻译,可直接翻译单词或句子

使用的百度翻译API

使用：

1. 直接输入文本

    >> ./trs.py "Hello World"
    >> 你好世界

    >> ./trs.py "你好世界"
    >> Hello world

2. 翻译文件

    >> echo "Hello World" > test.txt
    >> ./trs.py test.txt
    >> 你好世界

3. 推荐使用方法

    >> sudo cp ./trs.py /usr/bin/trs
    >> sudo chmod +x /usr/bin/trs

    >> trs "Hello World"
    >> 你好世界

    >> trs test.txt
    >> 你好世界

"""

# sys
import os
import sys
import urllib
import urllib2
import json


class Translation(object):

    """ 翻译 """

    # config
    BASE_URL = "http://openapi.baidu.com/public/2.0/bmt/translate"
    API_KEY = "GM3N6zSue8SvSFU7xhWTZPQ9"

    def __init__(self, input_args, from_="auto", to="auto"):
        self.from_ = from_
        self.to = to
        self.timeout = 10
        if len(input_args) != 2:
            print 'Error: Enter a or sentence!'
            sys.exit(1)
        self.word_or_sentence = self.parse_args(input_args)
        self.translate()

    def parse_args(self, input_args):
        """解析命令
        """
        word_or_file = input_args[1]
        # 是否是文件
        if os.path.exists(word_or_file):
            with open(word_or_file) as fop:
                return fop.read().strip()
        return word_or_file

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
        params = {
            "from": self.from_,
            "to": self.to,
            "client_id": self.API_KEY,
            "q": self.word_or_sentence,
        }
        data = urllib.urlencode(params)
        return self.BASE_URL, data

    def parse_result(self, res):
        """解析结果

        @res, dict, API返回的数据
        """
        if "error_code" in res:
            print "Error: %s %s" \
                % (res["error_msg"], res["error_code"])
            sys.exit(1)
        results = res["trans_result"]
        dest = '\n'.join([item["dst"] for item in results])
        print dest


def main():
    """ main """
    Translation(sys.argv)

if __name__ == "__main__":
    main()
