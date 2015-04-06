# 描述

基于命令行的快速翻译，可直接翻译`单词`或`句子`。

使用的`百度翻译API`。

# 使用：

- 直接输入文本

        > ./trs.py "Hello World"
        > 你好世界

        > ./trs.py "你好世界"
        > Hello world

- 翻译文件

        > echo "Hello World" > test.txt
        > ./trs.py test.txt
        > 你好世界

- **推荐使用方法**

        > sudo cp ./trs.py /usr/bin/trs
        > sudo chmod +x /usr/bin/trs

        > trs "Hello World"
        > 你好世界

        > trs test.txt
        > 你好世界
