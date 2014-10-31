__author__ = 'Feely'

#!/usr/bin/python
#-*- coding: utf8 -*-

from lxml import etree
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr
import mechanize
import logging

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

def bjkc():
    print "tjssc number:"
    url = "http://baidu.lecai.com/lottery/draw/view/557"
    #url ='http://kaijiang.cjcp.com.cn/cqssc'
    r = br.open(url)
    html = r.read()
    soup = BeautifulSoup(html)
    table_hot = soup.find('b')
    print table_hot.get_text()
    # print table_hot[2].get_text()
    # print table_hot.contents[0]
bjkc()

def gd11x5():
    """
    :rtype : str
    """
    try:
        r = br.open('http://baidu.lecai.com/lottery/draw/view/557')
        ssc_html = r.read().decode('utf-8')
        print ssc_html
    except Exception,err:
        print str(err)
        logging.error(str(err))
        return '0','0','0'
    else:
        #show the html title
        print br.title()
        #Show the response headers
        #print r.info()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u"//b[@id='jq_latest_draw_time']/text()")
        print result

gd11x5()