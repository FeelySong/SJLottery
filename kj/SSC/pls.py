__author__ = 'Feely'


__author__ = 'Feely'

#!/usr/bin/python
#-*- coding: utf8 -*-

from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr
import mechanize
import logging
import traceback

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

logging.basicConfig(filename='/tmp/kaijiang.log',level=logging.INFO)
logging.basicConfig(filename='/tmp/errkj.log',level=logging.ERROR)

def PLS():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    try:
        r = br.open('http://caipiao.163.com/order/pl3/')
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
        print draw_date_tmp
        draw_date=draw_date_tmp[5:10]
        print draw_date
        draw_code_tmp = d.xpath(u'//b[@class="c_ba2636"]/text()')[11].encode("utf-8")
        print draw_code_tmp
        draw_code=draw_code_tmp[0]+','+draw_code_tmp[2]+','+draw_code_tmp[4]
        print draw_code
        draw_time_tmp = d.xpath(u'//div[@class="n_kjgg"]/text()')[2].encode("utf-8")
        draw_time=draw_time_tmp[20:40]
        print draw_time
        print draw_date, draw_code, draw_time,datetime.now()
        logging.info(br.title())
        logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
        return draw_date,draw_code,draw_time