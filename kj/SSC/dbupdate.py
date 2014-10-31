#coding=utf-8
__author__ = 'Feely'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymssql
from datetime import datetime

# host='114.112.250.119'
# port='6000'
# user='dbadmin'
# password='1qaz2wsx'
# database='ibc'

host='223.252.163.80'
port='60000'
user='dbadmin'
password='1qaz2wsx'
database='ibc'

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
        if lottery_type=='SSC':
            sss='1,1,1'
            username='kefu1'
            wanfatype='投注重庆彩前三直选复式号码:'
            tzcodes=kjCodes[0:5]
            print type(tzcodes)
            querycode = 'select id,numberval,CharIndex(\'1,1,1\',numberval) from ibc.dbo.tborders where expect=\''+lottery_num+'\' and username=\''+ username+'\''
            # updatecode='update ibc.dbo.tborders set numberval=\''+tzcodes+'\' where expect=\''+lottery_num+'\' and username=\''+ username+'\' and numberval=\''+sss+'\''
            updatelog='update ibc.dbo.tbAdminlog set notes=\''+username +wanfatype+tzcodes+'\' where username=\''+username+'\' and notes=\''+username+wanfatype+sss+'\''
            print querycode
            cur = self.__GetConnect()
            cur.execute(querycode)
            resList = cur.fetchone()
            print resList
            if  resList:
                print resList[0],resList[1],resList[2]
                newcode=resList[1].replace(sss,tzcodes)
                updatecode='update ibc.dbo.tborders set numberval=\''+newcode+'\' where id=\''+str(resList[0])+'\''
                print updatecode
                cur.execute(updatecode)
                self.conn.commit()
                updatelog='update ibc.dbo.tbAdminlog set notes=\''+username +wanfatype+newcode+'\' where username=\''+username+'\' and notes=\''+username+wanfatype+sss+'\''
                cur.execute(updatelog)
                self.conn.commit()
            kjtime_datetime=datetime.strptime(kjtime,"%Y-%m-%d %H:%M")
            cur.callproc('ibc.dbo.IsInfoExists',(lottery_type,lottery_num,kjCodes,kjtime_datetime,datetime.now(),))
            self.conn.commit()
            cur.callproc('ibc.dbo.SYSPaiJiang',(lottery_num,kjtime,kjCodes,lottery_type,))
            self.conn.commit()
            self.conn.close()
            return lottery_num
        else:
            cur = self.__GetConnect()
            kjtime_datetime=datetime.strptime(kjtime,"%Y-%m-%d %H:%M")
            cur.callproc('ibc.dbo.IsInfoExists',(lottery_type,lottery_num,kjCodes,kjtime_datetime,datetime.now(),))
            self.conn.commit()
            cur.callproc('ibc.dbo.SYSPaiJiang',(lottery_num,kjtime,kjCodes,lottery_type,))
            self.conn.commit()
            self.conn.close()
            return lottery_num
    # def SYSPaiJiang(self,SPname,kjExpect,kjTime,kjCode,ltType ):
    #     cur = self.__GetConnect()
    #     cur.callproc(SPname,(kjExpect,kjTime,kjCode,ltType,))
    #     self.conn.commit()
    #     self.conn.close()


