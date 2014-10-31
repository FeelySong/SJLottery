# coding=utf-8

import socket
from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr
import mechanize
import cookielib
import logging

socket.setdefaulttimeout(300)

#Browser
br = mechanize.Browser()
cj = cookielib.CookieJar()
br.set_cookiejar(cj)
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

logging.basicConfig(filename='/tmp/kaijiang.log',level=logging.INFO)
logging.basicConfig(filename='/tmp/errkj.log',level=logging.ERROR)

def drawnumber(ssc_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
    except Exception,err:
        error1= str(err)
        print ssc_type,error1
        logging.error(br.title())
        logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        draw_date = result[18:26]+result[27:30]
        draw_code = result[46:51]
        draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[65:81].strip()
        print draw_date, draw_code, draw_time,datetime.now()
        logging.info(br.title())
        logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
        #print result
        return draw_date,draw_code,draw_time


def tjssc():
    try:
        r = br.open("http://kaijiang.cjcp.com.cn/tjssc")
        html = r.read()
        soup = BeautifulSoup(html)
        table_hot = soup.find('td',attrs={"class":"qihao"})
        time_hot = soup.find ('td',attrs={"class":"time"})
        draw_time=time_hot.get_text()
        date_tmp=table_hot.get_text()
        draw_date=date_tmp[0:8]+'-0'+date_tmp[9:11]
        number1 = {}
        codes=''
        t1=0
        # print soup.find('td', text=table_hot.get_text()).parent.find_all('input')['value']
        while t1<5:
            number1[t1]=soup.find("td", text=table_hot.get_text()).parent.find_all('input')[t1]['value']
            codes=codes+number1[t1].strip()+','
            t1+=1
        draw_code=codes[:-1]
        print "tjssc number:"
        print draw_code,draw_date,draw_time
        return draw_code,draw_date,draw_time[:-3]
    except AttributeError as err:
        error=str(err)
        print error
        logging.error(br.title())
        logging.error(error)
        return '0','0','0'



def gd11x5(ssc_type):
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
    except Exception,err:
        error=str(err)
        print error
        logging.error(br.title())
        logging.error(error)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        #Show the response headers
        #print r.info()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        draw_date = result[15:27]
        draw_code = result[43:57]
        #draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[71:87].strip()
        print draw_date, draw_code, draw_time,datetime.now()
        logging.info(br.title())
        logging.info('date:%s code:%s time:%s',draw_date,draw_code,draw_time)
        #print result
        return draw_date,draw_code,draw_time

def PLS():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://caipiao.163.com/order/pl3/'
    try:
        r = br.open(url)
    except Exception,err:
        error1= str(err)
        print 'pls',error1
        logging.error(br.title())
        logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        draw_date_tmp = d.xpath(u'//b[@class="c_ba2636"]/text()')[10].encode("utf-8")
        #print draw_date_tmp
        draw_date=draw_date_tmp[5:10]
        #print draw_date
        draw_code_tmp = d.xpath(u'//b[@class="c_ba2636"]/text()')[11].encode("utf-8")
        #print draw_code_tmp
        draw_code=draw_code_tmp[0]+','+draw_code_tmp[2]+','+draw_code_tmp[4]
        #print draw_code
        draw_time_tmp = d.xpath(u'//div[@class="n_kjgg"]/text()')[2].encode("utf-8")
        draw_time=draw_time_tmp[20:40]
        #print draw_time
        print draw_date, draw_code, draw_time,datetime.now()
        logging.info(br.title())
        logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
        return draw_date,draw_code,draw_time