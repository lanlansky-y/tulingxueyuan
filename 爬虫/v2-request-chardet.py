'''
利用request下载页面
自动检测页面编码格式
'''
import urllib.request
import chardet
if __name__ == '__main__':
    url = 'https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052098167&courseId=1004987028'

    rsp = urllib.request.urlopen(url)
    html = rsp.read()
    #利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    #使用get()取值可以保证不会报错
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)