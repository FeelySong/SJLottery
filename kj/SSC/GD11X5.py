__author__ = 'Feely'

#!/usr/bin/python
#-*- coding: utf8 -*-

from lxml import etree
from datetime import datetime
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

logging.basicConfig(filename='/tmp/kaijiang.log',level=logging.INFO)
logging.basicConfig(filename='/tmp/errkj.log',level=logging.ERROR)



def gd11x5(ssc_type):
    """
    :rtype : str
    """
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
        ssc_html = r.read().decode('utf-8')
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
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        print result
        draw_date = result[15:27]
        draw_code = result[43:57]
        #draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[71:87].strip()
        print draw_date, draw_code, draw_time,datetime.now()
        logging.info(br.title())
        logging.info('date:%s code:%s time:%s',draw_date,draw_code,draw_time)
        #print result
        return draw_date,draw_code,draw_time

gd11x5('gd11x5')