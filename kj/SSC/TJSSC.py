
#coding:utf-8

import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
import sys
reload(sys)
sys.setdefaultencoding('GB2312')
import mechanize
import urllib2
from bs4 import BeautifulSoup
#Browser
br = mechanize.Browser()

#Browser options
br.set_handle_equiv(True)
##br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
#Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize.HTTPRefreshProcessor(), max_time=1)
#User-Agent
br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0")]

def tjssc():
    print "tjssc number:"
    url = "http://kaijiang.cjcp.com.cn/tjssc"
    #url ='http://kaijiang.cjcp.com.cn/cqssc'
    r = br.open(url)
    html = r.read()
    soup = BeautifulSoup(html)
    table_hot = soup.find('td',attrs={"class":"qihao"})
    time_hot = soup.find('td',attrs={"class":"time"})
    draw_time=time_hot.get_text()
    date_tmp=table_hot.get_text()
    draw_date=date_tmp[0:9]+'-0'+date_tmp[9:11]
    number1 = {}
    codes=''
    t1=0
    # print soup.find('td', text=table_hot.get_text()).parent.find_all('input')['value']
    while t1<5:
        number1[t1]=soup.find("td", text=table_hot.get_text()).parent.find_all('input')[t1]['value']
        print number1[t1]
        codes=codes+number1[t1].strip()+','
        t1+=1
    draw_code=codes[:-1]
    print draw_code,draw_date,draw_time
    return draw_code,draw_date,draw_time[:-3]
