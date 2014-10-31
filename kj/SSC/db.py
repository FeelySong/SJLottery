#coding=utf-8
__author__ = 'Feely'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymssql
from datetime import datetime

host='223.252.163.80'
port='60000'
user='jzviradmin'
password='1qaz2wsx'
database='ibc'

# host='114.112.250.119'
# port='6000'
# user='dbadmin'
# password='1qaz2wsx'
# database='ibc'

class MSSQL:
    def __init__(self):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
        if not self.database:
            raise(NameError,"No DataBase Info")
        self.conn = pymssql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"connect database failed")
        else:
            return cur

    def CallSP(self,lottery_type,lottery_num,kjCodes,kjtime):
        cur = self.__GetConnect()
        kjtime_datetime=datetime.strptime(kjtime,"%Y-%m-%d %H:%M")
        cur.callproc('ibc.dbo.IsInfoExists',(lottery_type,lottery_num,kjCodes,kjtime_datetime,datetime.now(),))
        self.conn.commit()
        cur.callproc('ibc.dbo.SYSPaiJiang',(lottery_num,kjtime,kjCodes,lottery_type,))
        self.conn.commit()
        self.conn.close()
        return lottery_num

    def PL3SP(self,lottery_type,lottery_num,kjCodes,kjtime):
        cur = self.__GetConnect()
        kjtime_datetime=datetime.strptime(kjtime,"%Y-%m-%d %H:%M")
        cur.callproc('ibc.dbo.IsInfoExists',(lottery_type,lottery_num,kjCodes,kjtime_datetime,datetime.now(),))
        self.conn.commit()
        cur.callproc('ibc.dbo.SYSPaiJiang',(lottery_num,kjtime,kjCodes,lottery_type,))
        self.conn.commit()
        self.conn.close()
        return lottery_num

    def JXCallSP(self,lottery_type,lottery_num,kjCodes,kjtime):
        cur = self.__GetConnect()
        kjtime_datetime=datetime.strptime(kjtime,"%Y-%m-%d %H:%M")
        cur.callproc('ibc.dbo.IsInfoExists', (lottery_type,kjCodes,lottery_num,kjtime_datetime,datetime.now(),))
        self.conn.commit()
        cur.callproc('ibc.dbo.SYSPaiJiang', (lottery_num,kjtime,kjCodes,lottery_type,))
        self.conn.commit()
        self.conn.close()
        return lottery_num

    # def SYSPaiJiang(self,SPname,kjExpect,kjTime,kjCode,ltType ):
    #     cur = self.__GetConnect()
    #     cur.callproc(SPname,(kjExpect,kjTime,kjCode,ltType,))
    #     self.conn.commit()
    #     self.conn.close()


