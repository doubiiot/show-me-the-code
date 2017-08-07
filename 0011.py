'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
word_buffer = []
with open("keywords.txt") as fp:
    for word in fp:
        word_buffer.append(word.strip('\n'))
while True:
    inword = input()
    str = ''
    for buff in word_buffer:
        if buff.strip() in inword:
            print("Freedom")
            for i in range(len(buff)):
                str += '*'
            inword = inword.replace(buff,str)
        else:
            pass
    print(inword)