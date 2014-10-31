# coding=utf-8
__author__ = 'Feely'

import time
import multiprocessing
import sys

import DrawNO
from SSC import db
import GDSFC


reload(sys)
sys.setdefaultencoding('utf-8')
sys.excepthook = lambda *args: None
STDERR = sys.stderr


#重庆时时彩
def ssc_drawnumber(ssc_type,db_ssc_type):
    ms_cqssc= db.MSSQL()
    returndate=''
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.drawnumber(ssc_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=ms_cqssc.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
        # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
        # time.sleep(1)
        # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
        time.sleep(30)

def jxssc_drawnumber(ssc_type,db_ssc_type):
    ms_jxssc= db.MSSQL()
    returnDate=''
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_code, draw_date, draw_time_str= DrawNO.drawnumber(ssc_type)
        if  draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_jxssc.JXCallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)

def gd11x5(ssc_type,db_ssc_type):
    ms_gd11x5= db.MSSQL()
    returndate=''
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.gd11x5(ssc_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=ms_gd11x5.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)

def tjssc_drawnumber(db_ssc_type):
    ms_jxssc= db.MSSQL()
    returnDate=''
    while True:
        #调用爬虫，获取开奖信息
        draw_code, draw_date, draw_time_str= DrawNO.tjssc()
        if  draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_jxssc.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)
#排列三
def pls_drawnumber(db_type):
    ms_pls= db.MSSQL()
    returnDate=''
    while True:
        #调用爬虫，获取开奖信息
        draw_date,draw_code, draw_time_str= DrawNO.PLS()
        if draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_pls.PL3SP(lottery_type=db_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)


#GDSFC
def gdsf_drawnumber(gdsf_db_type):
    ms_gdsf= db.MSSQL()
    returnDate=''
    while True:
        # #调用爬虫，获取开奖信息
        draw_date,draw_code,draw_time_str= GDSFC.drawnumber()
        if  draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_gdsf.CallSP(lottery_type=gdsf_db_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
        time.sleep(30)


def main():
    """

    :rtype : Null
    """
    #重庆时时彩
    ssc_type='cqssc'
    db_ssc_type='SSC'
    jobs=[]
    for i in range(2):
        p_cq=multiprocessing.Process(name='CQSSC',target=ssc_drawnumber,args=(ssc_type,db_ssc_type,))
        jobs.append(p_cq)
        p_cq.start()
        p_cq.join(timeout=10)

    # #排列三
    # db_type='PLS'
    # p_cq=multiprocessing.Process(name='PL3',target= pls_drawnumber,args=(db_type,))
    # p_cq.start()
    # p_cq.join(timeout=10)

    # #天津时时彩
    # db_ssc_type='TSC'
    # p_tj=multiprocessing.Process(name='TJSSC',target=tjssc_drawnumber,args=(db_ssc_type,))
    # p_tj.start()
    # p_tj.join(10)
    #
    # #江西时时彩
    # ssc_type='jxssc'
    # db_ssc_type='XSC'
    # p_jx=multiprocessing.Process(name='JXSSC',target=jxssc_drawnumber,args=(ssc_type,db_ssc_type,))
    # p_jx.start()
    # p_jx.join(10)
    #
    # #广东十分彩
    # gdsf_db_type='GDS'
    # p_gdsf=multiprocessing.Process(name='GDSFC',target=gdsf_drawnumber,args=(gdsf_db_type,))
    # p_gdsf.start()
    # p_gdsf.join(timeout=10)
    #
    # #广东11选5
    # ssc_type='gd11x5'
    # db_11x5_type='SYX'
    # p_11x5=multiprocessing.Process(name='GD11X5',target=gd11x5,args=(ssc_type,db_11x5_type,))
    # p_11x5.start()
    # p_11x5.join(10)

if __name__ == "__main__":
    main()