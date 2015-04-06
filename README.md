# 描述

基于命令行的快速翻译，可直接翻译`单词`或`句子`。

使用的`百度翻译API`。

# 说明

- `trs.py`: 翻译，可翻译单词或句子，支持文件翻译；
- `dc.py`: 主要是词典解析，指定单词翻译；

# 使用：

## 翻译句子或单词

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

## 词典：

- 直接待翻译的单词

        > ./dc.py "Hello"
        >   ##################################################
            hello [英]:[hə'ləʊ] [美]:[hɛˈlo, hə-]
            int. 哈喽，喂; 你好，您好; 表示问候; 打招呼
            n. “喂”的招呼声或问候声
            vi. 喊“喂”
            ##################################################

        > ./dc.py "你好"
        >   ##################################################
            你好 [nǐ hǎo]
            hello; hi; How do you do!
            ##################################################

- **推荐使用方法**

        > sudo cp ./dc.py /usr/bin/dc
        > sudo chmod +x /usr/bin/dc

        > dc "Hello"
        >   ##################################################
            hello [英]:[hə'ləʊ] [美]:[hɛˈlo, hə-]
            int. 哈喽，喂; 你好，您好; 表示问候; 打招呼
            n. “喂”的招呼声或问候声
            vi. 喊“喂”
            ##################################################

        > dc "你好"
        >   ##################################################
            你好 [nǐ hǎo]
            hello; hi; How do you do!
            ##################################################
