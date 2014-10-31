__author__ = 'Feely'

#!/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import mechanize
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


def drawnumber():
    try:
        #Open website
        r = br.open('http://kjh.cailele.com/history_klsf.aspx')
        ssc_html = r.read()
    except Exception,err:
        print str(err)
        return '0','0','0'
    else:
        #show the html title
        print br.title()
        soup = BeautifulSoup(ssc_html)
        table_hot = soup.find('td', attrs={"height": "30"})
        i=0
        number = []
        for td in soup.find('td',text=table_hot.get_text()).parent.find_all('td'):
            number.append(td.text)
            i += 1
        draw_date=number[0].strip()
        draw_time=number[1].strip()
        draw_code_tmp=number[2].replace("\n",",")
        draw_code=draw_code_tmp[1:]
        print draw_date,draw_code,draw_time
        return draw_date,draw_code,draw_time