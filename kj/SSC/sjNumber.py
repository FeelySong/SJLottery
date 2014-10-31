# coding=utf-8
__author__ = 'Feely'

import time
import multiprocessing
import sys

import DrawNO
import conn
import GDSFC


reload(sys)
sys.setdefaultencoding('utf-8')
sys.excepthook = lambda *args: None
STDERR = sys.stderr


#重庆时时彩
def ssc_drawnumber(ssc_type,db_ssc_type):
    returndate=''
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.drawnumber(ssc_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=conn.kjdata(t2=draw_code,cid=db_ssc_type,t1=draw_date,t3=draw_time_str)
            time.sleep(180)
        # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
        # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
        # time.sleep(1)
        # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
        time.sleep(30)

def main():
    """

    :rtype : Null
    """
    #重庆时时彩
    ssc_type='cqssc'
    db_ssc_type='1'
    jobs=[]
    for i in range(2):
        p_cq=multiprocessing.Process(name='CQSSC',target=ssc_drawnumber,args=(ssc_type,db_ssc_type,))
        jobs.append(p_cq)
        p_cq.start()
        p_cq.join(timeout=10)
if __name__ == "__main__":
    main()