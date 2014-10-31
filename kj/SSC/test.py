#coding=utf-8

import socket
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr
import mechanize
import cookielib

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
br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0 FirePHP/0.7.4"),
                 ("Content-Type","text/json; charset=utf-8")]


r = br.open('http://www.lecai.com/lottery/draw/ajax_get_latest_draw_html.php?lottery_type=200')

print r.read()
