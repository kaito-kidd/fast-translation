#!/usr/bin/env python
# -*- coding: utf8 -*-

"""基于命令行的单词翻译。

使用：

1. 直接输入文本

    >> ./dc.py "Hello"
    >>  ##################################################
        hello [英]:[hə'ləʊ] [美]:[hɛˈlo, hə-]
        int. 哈喽，喂; 你好，您好; 表示问候; 打招呼
        n. “喂”的招呼声或问候声
        vi. 喊“喂”
        ##################################################

    >> ./dc.py "你好"
    >>  ##################################################
        你好 [nǐ hǎo]
        hello; hi; How do you do!
        ##################################################

2. 推荐使用方法

    >> sudo cp ./dc.py /usr/bin/dc
    >> sudo chmod +x /usr/bin/dc

    >> dc "Hello"
    >>  ##################################################
        hello [英]:[hə'ləʊ] [美]:[hɛˈlo, hə-]
        int. 哈喽，喂; 你好，您好; 表示问候; 打招呼
        n. “喂”的招呼声或问候声
        vi. 喊“喂”
        ##################################################

    >> dc "你好"
    >>  ##################################################
        你好 [nǐ hǎo]
        hello; hi; How do you do!
        ##################################################

"""

# sys
import sys
import urllib

# my
from parser import Parser


class Dictionary(Parser):

    """ 词典 """

    # config
    BASE_URL = "http://openapi.baidu.com/public/2.0/translate/dict/simple"

    def __init__(self, input_args):
        args_errmsg = "Enter a word!"
        super(Dictionary, self).__init__(
            input_args, args_errmsg=args_errmsg)

    def parse_args(self, input_args):
        """解析命令
        """
        word = input_args[1].strip()
        if " " in word:
            print 'Error: Enter a word!'
            sys.exit(1)
        return word

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
        url = "%s?%s" % (self.BASE_URL, data)
        return url, None

    def parse_result(self, res):
        """解析结果

        @res, dict, API返回的数据
        """
        if res["errno"] != 0:
            print "Error: %s %s" % (res["errno"], res["errmsg"])
            sys.exit(1)
        data = res["data"]
        if not data:
            print "No results!"
            sys.exit(1)
        to, from_ = res["to"], res["from"]
        result = self._pack_content(to, from_, data)
        print result

    def _pack_content(self, to, from_, data):
        """组装内容

        @to, str, to
        @from_, str, from
        @data, dict, data
        """
        word_name, symbols = data["word_name"], data["symbols"]
        symbol = symbols[0]
        parts = symbol["parts"]
        # 中 --> 英
        if to == "zh" and from_ == "en":
            head = u"%s [英]:[%s] [美]:[%s]" \
                % (word_name, symbol["ph_en"], symbol["ph_am"])
            line_body = []
            for item in parts:
                prop = item["part"]
                content = "; ".join([mean for mean in item["means"]])
                line_body.append("%s %s" % (prop, content))
            body = "\n".join(line_body)
        # 英 --> 中
        elif to == "en" and from_ == "zh":
            head = "%s [%s]" % (word_name, symbol["ph_zh"])
            body = "; ".join([line for line in parts[0]["means"]])
        else:
            print "Error: This operation is not supported!"
            sys.exit(1)
        prefix, suffix = "#" * 50, "#" * 50
        return "%s\n%s\n%s\n%s" % (prefix, head, body, suffix)


def main():
    """ main """
    Dictionary(sys.argv)

if __name__ == "__main__":
    main()
