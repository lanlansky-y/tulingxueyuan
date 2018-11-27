import urllib.request

if __name__ == '__main__':
    url = 'https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052096226&courseId=1004987028'
    rsp = urllib.request.urlopen(url)
    print(type(rsp))    #此时rsp返回的是一个实例
    print(rsp)
    html = rsp.read()

#后半段
    print('url: {0}'.format(rsp.geturl()))
    print('info: {0}'.format(rsp.info()))
    print('code: {0}'.format(rsp.getcode()))