from urllib import request

if __name__ == '__main__':
    url = "https://study.163.com/my"

    headers = {
        'cookie':'_ntes_nnid=1fc32a53db6fa0c1495233a88ce374c2,1536129170361; _ntes_nuid=1fc32a53db6fa0c1495233a88ce374c2; EDUWEBDEVICE=98a43cc69e4c4522936fc31139e7e6fb; __guid=129633230.2560812684986307600.1536288597937.7202; __f_=1536288739219; P_INFO=yyz865676567@vip.qq.com|1536297512|1|study|00&99|zhj&1532608836&ty#zhj&330100#10#0#0|&0||yyz865676567@vip.qq.com; videoResolutionType=3; vjuids=-b62e57862.165c13eedd6.0.80080e9dc73d5; __utmz=129633230.1538096876.13.2.utmcsr=cp-400000000387008|utmccn=commission|utmcmd=share; UM_distinctid=166574240fc7a5-032263aa36634b-454c092b-1fa400-166574240fd7e9; __gads=ID=b992867b1ea5bdc3:T=1539062296:S=ALNI_MbQ9L7YiqFKP_PGC22RFa6Pf3BmPA; hasVolume=true; Province=0571; City=0571; vjlast=1536545451.1541149802.11; vinfo_n_f_l_n3=26b5ae16de1d2f61.1.7.1536129170370.1540370129879.1541149837767; sideBarPost=695; NNSSPID=fda1de172bfb402b8145c5c9a5b08a6e; NTESSTUDYSI=2a8cc8fc6d394a7d9d920eaf218e0265; STUDY_INFO="yyz865676567@vip.qq.com|-1|1019407291|1541467435900"; STUDY_SESS="SwHxFWmMfqHaKw6ggbpTKYAkVpK4/QOR4OAcdHMW8lMKwr+0CajbEnYhjBefeIrYLo0LbRKhLQ2028vxzIszCREjx9E1mQlutSgPoq+lQaaap+le6ugMpdg2fy3BdGGHpwGzOfG+zu4JcBptgnq2W2QxWNJptwo91x2CqHwDFK3fHzBS6ZsVuljVaKnkhaXLKmj1zRer5CpEuW7cMzJRxw=="; STUDY_PERSIST="d74BdF+Pe7JR73ISZtg9eawUJPdtN9SqcR2HgKkw+jaqvknZ/GNXJx18oProCHuaJSl8qw2qdgZylIZXDI6ZMJoZGlNWAu4y+wGX1jpt6NwqWH+uSVYdOcD3byGo77hSQEuDtGyQPkgirDkOjTRbabp64JlqDHGj26oqpsp3e8Dq8GpInEz8HKW1gkiHEDpm5nrQUS2RBGBThjxdVampVFl98chRpX7DRhpecJJiqCKruZvwZMgKvGCzy/gH3SmgP20F+4QccQRj+WrETZATZu0VYdPtCUeXsSUdD+5mTxI="; NETEASE_WDA_UID=1019407291#|#1471955060644; __utmc=129633230; STUDY_NOT_SHOW_PROMOTION_WIN=true; videoVolume=1; monitor_count=21; __utma=129633230.1235983935.1536288598.1541467670.1541493682.61; NTES_STUDY_YUNXIN_ACCID=s-1019407291; NTES_STUDY_YUNXIN_TOKEN=9ad0240c5834773d3fe5627b28285138; __utmb=129633230.4.10.1541493682'
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(html)