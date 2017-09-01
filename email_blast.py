# -*- coding:utf-8 -*-
# @Time    : 2017/8/31 19:47
# @Author  : zlmfslx
# @File    : request.py


import requests
from bs4 import BeautifulSoup as BS

def email():
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'自己填写自己的',
    'Host':'mail.ym.163.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    html = requests.get('http://mail.ym.163.com/jy3/address/oablist.jsp?sid=A0fAf708x6R4z2KEegYkf-4ICzrjaAkV&dn=xx00_com',headers=headers)
    number = 1#计算邮箱个数
    soup = BS(html.content,'lxml')
    print html.content
    ahtml = soup.find_all(name='a',attrs={'class':'qiye_Dname'})
    for a in ahtml:
        #print a.text,  哪个部门
        url = 'http://mail.ym.163.com/jy3/address/'+a['href']
        employee = requests.get(url,headers=headers)
        email_html = BS(employee.content,'lxml')
        emails = email_html.find_all(name='a',attrs={'class':'qiye_Oname'})

        for i in emails:
            print i.text  #哪个员工姓名
            email = i['href'].split('&email=')[1]#员工邮箱
            #name = email.split('@')
            number = number +1
            #print number
            return email






if __name__ =='__main__':
    print email()


